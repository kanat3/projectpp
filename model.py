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

# 3X3X32 фильтров, RGB 64x64 размер изображения, функция активации relu.
baseline_model.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(64,64,3), activation='relu'))
# Функция maxpool выделяет максимальные значения, тем самым обобщая признаки изображения.
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
baseline_model.add(MaxPooling2D(pool_size=(2, 2)))

baseline_model.add(Flatten()) #Выравнивает вход. Не влияет на размер партии.
baseline_model.add(Dense(512, activation='relu')) #Просто обычный плотно связанный слой NN. 512 - размерность выходного пространства.

baseline_model.add(Dense(128, activation='relu')) #Fully Connected Layer

baseline_model.add(Dense(2, activation='softmax')) #Softmax — это обобщение логистической функции для многомерного случая.

baseline_model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.SGD(learning_rate=0.01), metrics=['accuracy'])
#Функция потерь - категориальная перекрестная энтропия,optimizer.SGD - стохастический оптимизатор градиентного спуска.
#Включает в себя поддержку импульса, затухания скорости обучения и импульса Нестерова. learning_rate: float >= 0. Скорость обучения.
#Метрика — это функция, которая используется для оценки работы вашей модели. Метрические функции предоставляются в параметре метрики при компиляции модели.
#accuracy - Вычисляет, как часто предсказания равны меткам.
