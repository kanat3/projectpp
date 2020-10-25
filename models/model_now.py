import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import regularizers, optimizers
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.models import load_model
from keras.layers.normalization import BatchNormalization

def model_gender():
    model = Sequential()
    
    model.add(Conv2D(filters=3, kernel_size=(4, 4), input_shape=(288, 432, 3), activation='relu')) 
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=32, kernel_size=(4, 4), activation='relu')) 
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu')) 
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu')) 
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=256, kernel_size=(2, 2), activation='relu')) 
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten()) #Fully Connected Layer
    model.add(Dense(77, activation='relu'))
    
    model.add(Dense(2, activation='softmax'))

    model.compile(loss='binary_crossentropy', optimizer= 'adam', metrics=['accuracy'])
    return model
