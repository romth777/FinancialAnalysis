# -*- coding:utf-8 -*-
import os
import json

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np
from keras.utils.visualize_util import plot
from keras.callbacks import ModelCheckpoint, EarlyStopping

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './data/KerasFirstTest'))

model = Sequential()
model.add(Dense(output_dim=1, input_dim=1, init="glorot_uniform"))
model.add(Activation("sigmoid"))

model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.01, momentum=0.1, nesterov=True))

x_train = np.array([1])
y_train = np.array([0])
x_train = x_train.reshape(x_train.shape[0], 1)
y_train = y_train.reshape(y_train.shape[0], 1)

x_test = np.array([1])
y_test = np.array([0])
x_test = x_test.reshape(x_test.shape[0], 1)
y_test = y_test.reshape(y_test.shape[0], 1)

checkpointer = ModelCheckpoint(filepath=name + "\\sample_model.hdf5", verbose=1, save_best_only=True)
earlystopping = EarlyStopping(monitor='val_loss', patience=5, verbose=0, mode='auto')
hist = model.fit(x_train, y_train, nb_epoch=100, batch_size=1, validation_data=(x_test, y_test), callbacks=[checkpointer, earlystopping], show_accuracy=True)

# save models and history
plot(model, to_file=name + '\\sample_model.png')
with open(name + '\\sample_loss.json', 'w') as fp:
    json.dump(hist.history, fp)

