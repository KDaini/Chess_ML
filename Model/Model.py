import gc

import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as layers
from tensorflow.keras import models as md
from datetime import datetime
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv3D, \
    AveragePooling3D, MaxPooling3D, InputLayer, Softmax, Attention, BatchNormalization, LSTM, GlobalAveragePooling1D, Conv2D

data_path = "E:/Chess Games Downloaded/Dataset/"
black_path = "E:/Chess Games Downloaded/Dataset/Black Win/"
white_path="E:/Chess Games Downloaded/Dataset/White Win/"
draw_path="E:/Chess Games Downloaded/Dataset/Draw/"

# np.set_printoptions(threshold=np.inf)

def init_model():

    labels = np.load('E:/Chess Games Downloaded/2022 Data/fractions/labels.npy', allow_pickle=True)
    gameData = np.load('E:/Chess Games Downloaded/2022 Data/fractions/dataset.npy', allow_pickle=True)
    print(gameData.shape)
    print(labels.shape)
    gameData=np.reshape(gameData,(45000,1,8,400,8))
    #gameData = tf.expand_dims(tf.transpose(gameData, [0, 1, 3, 2]), axis=-4)
    #train_data = tf.data.Dataset.from_tensor_slices((gameData, labels))
    model = tf.keras.Sequential()
    model.add(Conv3D(filters=8, kernel_size=(1, 8, 8),strides=4,input_shape=(1,8,400,8),activation="relu"))
    model.add(Dense(64,activation="relu"))
    model.add(Flatten())
    model.add(Dense(3,activation="softmax"))
    model.add(Flatten())

    opt = Adam(learning_rate=0.0001)
    model.compile(
        optimizer=opt,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"])
    print("Fitting Model...")
    model.fit(gameData,labels, validation_split=0.2, batch_size=5, epochs=15)  #   validation_split=0.3
    model.save('C:/Users/m00ki/PycharmProjects/Chess_ML/Model/')
    return


def into_model(input) -> int:
    model = tf.keras.Sequential()
    model = tf.keras.models.load_model('C:/Users/m00ki/PycharmProjects/Chess_ML/Model/')

    retVal = tf.keras.Model.predict(model, batch_size=None)
    x = model.save('/Model/mnist_model')
    return retVal

init_model()
