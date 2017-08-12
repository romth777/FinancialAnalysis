# -*- coding:utf-8 -*-
import chainer
import chainer.functions as F
import chainer.links as L


class MnistMLP(chainer.Chain):

    """An example of multi-layer perceptron for MNIST dataset.

    This is a very simple implementation of an MLP. You can modify this code to
    build your own neural net.

    """
    def __init__(self, n_in, n_units, n_out):
        super(MnistMLP, self).__init__(
            l1=L.Linear(n_in, n_units),
            l2=L.Linear(n_units, n_units),
            l3=L.Linear(n_units, n_out),
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)


class MnistMLPParallel(chainer.Chain):

    """An example of model-parallel MLP.

    This chain combines four small MLPs on two different devices.

    """
    def __init__(self, n_in, n_units, n_out):
        super(MnistMLPParallel, self).__init__(
            first0=MnistMLP(n_in, n_units // 2, n_units).to_gpu(0),
            first1=MnistMLP(n_in, n_units // 2, n_units).to_gpu(1),
            second0=MnistMLP(n_units, n_units // 2, n_out).to_gpu(0),
            second1=MnistMLP(n_units, n_units // 2, n_out).to_gpu(1),
        )

    def __call__(self, x):
        # assume x is on GPU 0
        x1 = F.copy(x, 1)

        z0 = self.first0(x)
        z1 = self.first1(x1)

        # sync
        h0 = z0 + F.copy(z1, 0)
        h1 = z1 + F.copy(z0, 1)

        y0 = self.second0(F.relu(h0))
        y1 = self.second1(F.relu(h1))

        # sync
        y = y0 + F.copy(y1, 0)
        return y


class LSTM(chainer.Chain):

    """Recurrent neural net languabe model for penn tree bank corpus.
    This is an example of deep LSTM network for infinite length input.
    """
    def __init__(self, n_vocab, n_units, train=True):
        super(LSTM, self).__init__(
            embed=L.EmbedID(n_vocab, n_units),
            l1=L.LSTM(n_units, n_units),
            l2=L.Linear(n_units, 1),
        )
        self.train = train

    def reset_state(self):
        self.l1.reset_state()

    def __call__(self, x):
        h0 = self.embed(x)
        h1 = self.l1(h0)
        y = self.l2(h1)
        return y


class Zundoko(chainer.Chain):
    def __init__(self, input_num, hidden_num, output_num):
        super(Zundoko, self).__init__(
            word=L.Linear(input_num, hidden_num),
            lstm=L.Linear(hidden_num, hidden_num),
            linear=L.Linear(hidden_num, hidden_num),
            out=L.Linear(hidden_num, output_num),
        )

    def __call__(self, x, train=True):
        h1 = self.word(x)
        h2 = F.relu(self.linear(h1))
        h3 = F.relu(self.linear(h2))
        return self.out(h3)

    def reset_state(self):
        # self.lstm.reset_state()
        pass