import os
import cv2
import numpy as np

def load_data(data_dir, classes, image_width, image_height):
    images = []
    labels = []

    for class_name in classes:
        class_dir = os.path.join(data_dir, class_name)
        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            image = cv2.imread(image_path)
            if image is None:
                continue
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (image_width, image_height))
            images.append(image)
            labels.append(classes.index(class_name))

    images = np.array(images)
    labels = np.array(labels)

    return images, labels
