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
