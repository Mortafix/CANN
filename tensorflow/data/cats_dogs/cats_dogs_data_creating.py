import cv2
import os
import numpy as np
from random import shuffle
from tqdm import tqdm

# Settings
# Database link : https://www.kaggle.com/c/dogs-vs-cats/data
HOME_DIR = '/Users/Moris/Downloads/'
TRAIN_DIR = HOME_DIR+'train'
TEST_DIR = HOME_DIR+'test'
IMG_SIZE = 50

# Create encoded vector from image name
def create_label(image_name):
    word_label = image_name.split('.')[-3]
    if word_label == 'cat':
        return np.array([1,0])
    elif word_label == 'dog':
        return np.array([0,1])

# Image processing
def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        path = os.path.join(TRAIN_DIR, img)
        img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
        training_data.append([np.array(img_data), create_label(img)])
    shuffle(training_data)
    np.save('cats_dogs_train.npy', training_data)
    return training_data

def create_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR,img)
        img_num = img.split('.')[0]
        img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
        testing_data.append([np.array(img_data), img_num])     
    shuffle(testing_data)
    np.save('cats_dogs_test.npy', testing_data)
    return testing_data

create_train_data()
create_test_data()