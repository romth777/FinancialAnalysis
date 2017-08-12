# -*- coding:utf-8 -*-
import sys
import os
import json

from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.utils.visualize_util import plot
from keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np

sys.path.append(os.pardir + "\\" + os.pardir + '\\MyFirstChainer\\src')
import ChainerDataManager

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './data/MyFirstKeras'))

cdm = ChainerDataManager.ChainerDataManager(name + "\\stock_with_timestep.pkl")

# Prepare dataset
print('load Stock dataset')
stocks = cdm.load_stock_data("2016-04-01")
stocks['data'] = stocks['data'].astype(np.float32)
stocks['target'] = stocks['target'].astype(np.int32)

# NはTrainデータ数
N = cdm.num_train
x_train, x_test = np.split(stocks['data'], [N])
y_train, y_test = np.split(stocks['target'], [N])
N_test = y_test.size

# keras code
print('set model')

model = Sequential()
##RNN
# expected input data shape: (batch_size, timesteps, data_dim)
# data_dim = 20
# timesteps = 20
# nb_classes = 3
# model.add(LSTM(200, return_sequences=True,
#                input_shape=(timesteps, data_dim)))  # returns a sequence of vectors of dimension 200
# model.add(LSTM(100, return_sequences=True))  # returns a sequence of vectors of dimension 100
# model.add(LSTM(50, return_sequences=True))  # returns a sequence of vectors of dimension 50
# model.add(LSTM(20, return_sequences=True))  # returns a sequence of vectors of dimension 20
# model.add(LSTM(10))  # return a single vector of dimension 10
# model.add(Dense(nb_classes, activation='sigmoid'))

## NN
model.add(Dense(output_dim=300, input_dim=400, init="glorot_uniform", activation="sigmoid"))
model.add(Dense(output_dim=200, input_dim=300, init="glorot_uniform", activation="sigmoid"))
model.add(Dense(output_dim=100, input_dim=200, init="glorot_uniform", activation="sigmoid"))
model.add(Dense(output_dim=50, input_dim=100, init="glorot_uniform", activation="sigmoid"))
model.add(Dense(output_dim=20, input_dim=50, init="glorot_uniform", activation="sigmoid"))
model.add(Dense(output_dim=10, input_dim=20, init="glorot_uniform", activation="sigmoid"))
model.add(Dense(output_dim=3, input_dim=10, init="glorot_uniform", activation="sigmoid"))

print('compile model')
model.compile(loss='mean_squared_error', optimizer='rmsprop')

print('fit model')
checkpointer = ModelCheckpoint(filepath=name + "\\stock_model_nn.hdf5", verbose=1, save_best_only=True)
earlystopping = EarlyStopping(monitor='val_loss', patience=5, verbose=0, mode='auto')
hist = model.fit(x_train, y_train,
                 batch_size=50, nb_epoch=5000, show_accuracy=True,
                 validation_data=(x_test, y_test), callbacks=[checkpointer, earlystopping])

# save models and history
plot(model, to_file=name + '\\stock_model_nn.png')
with open(name + '\\stock_loss_nn.json', 'w') as fp:
    json.dump(hist.history, fp)
