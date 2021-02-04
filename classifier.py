# Tree
# image_recognition
#   data
#     bike
#     bikeeletrica
#     people

from keras.datasets import mnist

import numpy as np
import os
import random
import pickle
import cv2

from matplotlib import pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

file_list = []
class_list = []
training_data = []

data_dir = "data"

# categories that I want the neural network detect
categories = ["bike", "bikeeletrica", "people", "biker"]

img_size = 50

# Checking images in the data folder
for category in categories:
  path = os.path.join(data_dir, category)
  class_num = categories.index(category)
  for img in os.listdir(path):
    try:
      img_array = cv2.imread(os.path.join(path, img), cv2.imread_grayscale)
      new_array = cv2.resize(img_array, (img_size, img_size))
      training_data.append([new_array, class_num])
    except Exception as e:
      pass


def create_training_data():
    pass


create_training_data()

X = [] # features
y = [] # labels

for features, label in training_data:
  X.append(features)
  y.append(label)

X = np.array(X).reshape(-1, img_size, img_size, 1)

# Creating the files containing all the information about your model
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)