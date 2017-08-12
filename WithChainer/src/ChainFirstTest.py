# -*- coding:utf-8 -*-
from __future__ import print_function
import argparse

import numpy as np
import six

import chainer
from chainer import cuda
import chainer.links as L
import chainer.function as F
from chainer import optimizers
from chainer import serializers

import ChainerDataManager
import net


parser = argparse.ArgumentParser(description='Chainer example: MNIST')
parser.add_argument('--initmodel', '-m', default='',
                    help='Initialize the model from given file')
parser.add_argument('--resume', '-r', default='',
                    help='Resume the optimization from snapshot')
parser.add_argument('--net', '-n', choices=('simple', 'parallel'),
                    default='simple', help='Network type')
parser.add_argument('--gpu', '-g', default=0, type=int,
                    help='GPU ID (negative value indicates CPU)')
args = parser.parse_args()

cdm = ChainerDataManager.ChainerDataManager()

n_epoch = 1000
hidden_num = 200 # 隠れ層のノードの数
output_num = 1
update_iteration = 20

zundoko = net.Zundoko(input_num=cdm.dim, hidden_num=hidden_num, output_num=output_num)

# Prepare dataset
print('load Stock dataset')
stocks = cdm.load_stock_data()
stocks['data'] = stocks['data'].astype(np.float32)
stocks['target'] = stocks['target'].astype(np.int32)

# NはTrainデータ数
N = cdm.num_train
x_train, x_test = np.split(stocks['data'],   [N])
y_train, y_test = np.split(stocks['target'], [N])
N_test = y_test.size

# Prepare multi-layer perceptron model, defined in net.py
if args.net == 'simple':
    # model = L.Classifier(net.LSTM(cdm.dim, hidden_num))
    # model = L.Classifier(net.MnistMLP(cdm.dim, hidden_num, output_num))
    model = L.Classifier(net.Zundoko(cdm.dim, hidden_num, output_num))
    if args.gpu >= 0:
        cuda.get_device(args.gpu).use()
        model.to_gpu()
    xp = np if args.gpu < 0 else cuda.cupy
elif args.net == 'parallel':
    cuda.check_cuda_available()
    model = L.Classifier(net.MnistMLPParallel(cdm.dim, hidden_num, output_num))
    xp = cuda.cupy

# Setup optimizer
optimizer = optimizers.Adam(alpha=0.01)
optimizer.setup(model)

# Init/Resume
if args.initmodel:
    print('Load model from', args.initmodel)
    serializers.load_npz(args.initmodel, model)
if args.resume:
    print('Load optimizer state from', args.resume)
    serializers.load_npz(args.resume, optimizer)


def forward(train=True):
    loss = 0
    acc = 0
    if train:
        batch_size = 20
    else:
        batch_size = 1

    zundoko.reset_state()
    perm = np.random.permutation(N)
    for i in six.moves.range(0, N, batch_size):
        x = chainer.Variable(xp.asarray(x_train[perm[i:i + batch_size]]), volatile=not train)
        t = chainer.Variable(xp.asarray(y_train[perm[i:i + batch_size]]), volatile=not train)
        # y_var = zundoko(x, train=train)

        # Pass the loss function (Classifier defines it) and its arguments
        optimizer.update(model, x, t)

        loss += float(model.loss.data) * len(t.data)
        acc += float(model.accuracy.data) * len(t.data)

        # loss += F.softmax_cross_entropy(y_var, t)
        # acc += float(F.accuracy(y_var, t).data)
        # if not train:
        #     print input_words[x[0]]
        #     y = np.argmax(y_var.data[0])
        #     if output_words[y] != None:
        #         print output_words[y]
        #         break
        if train:
            optimizer.zero_grads()
            loss.backward()
            loss.unchain_backward()
            optimizer.update()
            print("train loss: {} accuracy: {}".format(loss.data, acc / update_iteration))
            loss = 0
            acc = 0

for iteration in range(n_epoch):
    print('epoch', iteration)
    loss, acc = forward()

# forward(train=False)



# # Learning loop
# for epoch in six.moves.range(1, n_epoch + 1):
#     print('epoch', epoch)
#
#     # training
#     perm = np.random.permutation(N)
#     sum_accuracy = 0
#     sum_loss = 0
#     for i in six.moves.range(0, N, batchsize):
#         x = chainer.Variable(xp.asarray(x_train[perm[i:i + batchsize]]))
#         t = chainer.Variable(xp.asarray(y_train[perm[i:i + batchsize]]))
#
#         # Pass the loss function (Classifier defines it) and its arguments
#         optimizer.update(model, x, t)
#
#         if epoch == 1 and i == 0:
#             with open('graph.dot', 'w') as o:
#                 g = computational_graph.build_computational_graph(
#                     (model.loss, ), remove_split=True)
#                 o.write(g.dump())
#             print('graph generated')
#
#         sum_loss += float(model.loss.data) * len(t.data)
#         sum_accuracy += float(model.accuracy.data) * len(t.data)
#
#     print('train mean loss={}, accuracy={}'.format(
#         sum_loss / N, sum_accuracy / N))
#
#     # evaluation
#     sum_accuracy = 0
#     sum_loss = 0
#     for i in six.moves.range(0, N_test, batchsize):
#         x = chainer.Variable(xp.asarray(x_test[i:i + batchsize]),
#                              volatile='on')
#         t = chainer.Variable(xp.asarray(y_test[i:i + batchsize]),
#                              volatile='on')
#         loss = model(x, t)
#         sum_loss += float(loss.data) * len(t.data)
#         sum_accuracy += float(model.accuracy.data) * len(t.data)
#
#     print('test  mean loss={}, accuracy={}'.format(
#         sum_loss / N_test, sum_accuracy / N_test))

# Save the model and the optimizer
print('save the model')
serializers.save_npz('stock.model', model)
print('save the optimizer')
serializers.save_npz('stock.state', optimizer)
