import cv2
import glob
import matplotlib.pyplot as plt
import numpy as np
from torch import int8

def load_image(file_name: str): 
    """
    load image(.png) and convert into np.ndarray
    """

    image = cv2.imread(file_name)
    image = image[..., ::-1] # BGR -> RGB
    image = image / 255.0 # float64
    image = image.astype('float32') # float64 -> float32
    return image

def load_dir(dir_name: str):
    """
    load all images in the dir 
    """
    output = []
    path_in_dir = glob.glob(dir_name + "/*.png")
    for path in path_in_dir:
        image = load_image(path)
        output.append(image)
    output = np.array(output)
    return output

def load_each_set(set_name: str):
    """
    load each dataset (train, val and test)
    """
    x = []
    y = []
    for label in [0, 1]:
        dataset = load_dir('Dataset/' + set_name + '/' + str(label) +'/')
        for data in dataset:
            x.append(data)
            y.append(np.array([label]).astype(np.uint8))
    return np.array(x), np.array(y)

def load_all_set():
    """
    load all dataset
    """
    x_train, y_train = load_each_set('train')
    x_val, y_val = load_each_set('val')
    x_test, y_test = load_each_set('test') 

    return x_train, y_train, x_val, y_val, x_test, y_test

def plot_image(image: np.ndarray):
    plt.figure(figsize=(7,7))
    plt.axis('off')
    plt.imshow(image, cmap="gray")