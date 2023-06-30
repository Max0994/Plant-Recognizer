import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model

# Загрузка обученной модели
model = load_model('plant_recognizer_model.h5')  # Замените 'path_to_model' на путь к вашей модели

image_width = 224  # Ширина изображений, используемая при обучении модели
image_height = 224  # Высота изображений, используемая при обучении модели

# Путь к папке с изображениями
folder_path = 'data/test'  # Замените 'folder_path' на путь к вашей папке с изображениями

# Перебор файлов в папке
for filename in os.listdir(folder_path):
    image_path = os.path.join(folder_path, filename)

    try:
        # Загрузка и предобработка изображения для классификации
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (image_width, image_height))  # Замените image_width и image_height на размеры, используемые при обучении модели
        image = image / 255.0  # Нормализация изображения

        # Классификация изображения
        prediction = model.predict(np.expand_dims(image, axis=0))
        predicted_class = np.argmax(prediction)

        # Определение результата
        if predicted_class == 0:
            print(f"Image {filename} in class 'plants'.")
        else:
            print(f"Image {filename} in class 'weed'.")

    except Exception as e:
        print(f"Ошибка при обработке изображения {filename}: {str(e)}")
