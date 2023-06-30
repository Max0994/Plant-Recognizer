import cv2
import numpy as np
from data_loader import load_data
from fit import train_model

data_dir = 'data'
classes = ['plants', 'weed']
image_width = 224
image_height = 224
num_epochs = 10


train_images, train_labels = load_data(data_dir, classes, image_width, image_height)


model = train_model(train_images, train_labels, classes, image_width, image_height, num_epochs)


model.save('plant_recognizer_model.h5')


