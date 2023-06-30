import tensorflow as tf

def train_model(train_images, train_labels, classes, image_width, image_height, num_epochs):

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_width, image_height, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(len(classes), activation='softmax')
    ])


    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])


    model.fit(train_images, train_labels, epochs=num_epochs)
    print(tf.config.list_physical_devices('GPU'))

    return model
