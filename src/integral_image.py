from PIL import Image
import numpy as np
import os

# read pixels into two dimentional array
# sum upper and left pixels + the pixel itself

def integral_img_from_file(image_file):
    """
    :param image_file:
    :return:
    """
    img = Image.open(image_file)
    img_array = np.asarray(img,np.uint8)
    integral_img_arry = integral_img_from_array(img_array)
    return integral_img_arry

def integral_img_from_array(img_array):
    """
    :param img_array:
    :return:
    """
    integral_img_array = np.zeros_like(img_array,np.int)
    for row in range(0, len(img_array)):
        for column in range(0, len(img_array)):
            if row == 0 and column == 0:
                integral_img_array[0, 0] = img_array[0, 0]
            elif row == 0:
                integral_img_array[row, column] = img_array[row, column] + integral_img_array[row, column - 1]
            elif column == 0:
                integral_img_array[row, column] = img_array[row, column] + integral_img_array[row - 1, column]
            else:
                integral_img_array[row, column] = img_array[row, column] + integral_img_array[row - 1, column] \
                                                  + integral_img_array[row, column - 1] - integral_img_array[
                                                      row - 1, column - 1]
    return integral_img_array
