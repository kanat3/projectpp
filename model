import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout 
#from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import regularizers, optimizers
from tensorflow.keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import TensorBoard
from kerastuner import HyperModel
from kerastuner.tuners import RandomSearch
# Tensorboard

baseline_model = Sequential()

# 3X3X32 filters, RGB 64x64 input image.
baseline_model.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(64,64,3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Flatten()) #Fully Connected Layer
baseline_model.add(Dense(512, activation='relu'))

baseline_model.add(Dense(128, activation='relu')) #Fully Connected Layer

baseline_model.add(Dense(2, activation='softmax'))

baseline_model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.SGD(learning_rate=0.01), metrics=['accuracy'])
