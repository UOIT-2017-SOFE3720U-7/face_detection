import numpy as np
from integral_image import *
import Haar_features
import os
import datetime
import pickle
from PIL import Image
from PIL import ImageDraw

# 2 squares value = sign * (A - B -2C + 2D + E - F)
# 3 squares value = sign * (A - B - 2C + 2D + H - G + 2E - 2F )
# 4 squares value = sign * (A - 2B + C - 2D + 4E - 2F + G - 2H + I

start_time = datetime.datetime.now()
print start_time
theta = -8
window_size = 19


print '###############################################################'
print 'theta = ', str(theta)
#weak_classifiers = Haar_features.all_features(19)
with open('two_rectangles_classifiers_9') as f:
    two_rectangles = pickle.load(f)
    #two_rectangles = two_rectangles[0:10]
with open('three_rectangles_classifiers_9') as f:
    three_rectangles = pickle.load(f)
    #three_rectangles = three_rectangles[0:10]
with open('four_squares_classifiers_9') as f:
    four_squares = pickle.load(f)

# Start of features valuation
#################################################################
def two_rectangles_values(integral_img):
    img_i_detection_array=[]
    #sum_array_len = len(sum_array)
    for j in xrange(0, len(two_rectangles)):
        feature = two_rectangles
        # 2 squares value = sign * (A - B -2C + 2D + E - F)
        classifier_value = feature[j][0] * (integral_img[feature[j][1][0], feature[j][1][1]] -
                                                          integral_img[feature[j][2][0], feature[j][2][1]] -
                                                          2 * integral_img[feature[j][3][0], feature[j][3][1]] +
                                                          2 * integral_img[feature[j][4][0], feature[j][4][1]] +
                                                          integral_img[feature[j][5][0], feature[j][5][1]] -
                                                          integral_img[feature[j][6][0], feature[j][6][1]])
        if classifier_value/(feature[j][7]*1.0) < theta:
            img_i_detection_array.append(1)
            #sum_array[j] = sum_array[j] + 1
        else:
            img_i_detection_array.append(-1)
            #sum_array[j] = sum_array[j] - 1
    return img_i_detection_array #, sum_array


def three_rectangles_values(integral_img,):
    img_i_detection_array = []
    #sum_array_len = len(sum_array)
    for j in xrange(0, len(three_rectangles)):
        feature = three_rectangles
        # 3 squares value = sign * (A - B - 2C + 2D + 2E - 2F - G + H)
        # new equation: value = sing * (((A - B - C + D + E - F - G + H)/2.0) - (C - D - E + F))
        classifier_value = feature[j][0] * (((integral_img[feature[j][1][0], feature[j][1][1]]
                                                          - integral_img[feature[j][2][0], feature[j][2][1]]
                                                          - integral_img[feature[j][3][0], feature[j][3][1]]
                                                          + integral_img[feature[j][4][0], feature[j][4][1]]
                                                          + integral_img[feature[j][5][0], feature[j][5][1]]
                                                          - integral_img[feature[j][6][0], feature[j][6][1]]
                                                          - integral_img[feature[j][7][0], feature[j][7][1]]
                                                          + integral_img[feature[j][8][0], feature[j][8][1]])/2.0)

                                                        - (integral_img[feature[j][3][0], feature[j][3][1]]
                                                           - integral_img[feature[j][4][0], feature[j][4][1]]
                                                           - integral_img[feature[j][5][0], feature[j][5][1]]
                                                           + integral_img[feature[j][6][0], feature[j][6][1]]))
        if classifier_value/(feature[j][9]*1.0) < theta:
            img_i_detection_array.append(1)
            #sum_array[j] = sum_array[j] + 1
        else:
            img_i_detection_array.append(-1)
            #sum_array[j] = sum_array[j] - 1
    return img_i_detection_array#, sum_array


def four_squares_values(integral_img):
    img_i_detection_array = []
    #sum_array_len = len(sum_array)
    for j in xrange(0, len(four_squares)):
        feature = four_squares
        # 4 squares value = sign * (A - 2B + C - 2D + 4E - 2F + G - 2H + I
        classifier_value = feature[j][0] * (integral_img[feature[j][1][0], feature[j][1][1]]
                                            - 2 * integral_img[feature[j][2][0], feature[j][2][1]]
                                            + integral_img[feature[j][3][0], feature[j][3][1]]
                                            - 2 * integral_img[feature[j][4][0], feature[j][4][1]]
                                            + 4 * integral_img[feature[j][5][0], feature[j][5][1]]
                                            - 2 * integral_img[feature[j][6][0], feature[j][6][1]]
                                            + integral_img[feature[j][7][0], feature[j][7][1]]
                                            - 2 * integral_img[feature[j][8][0], feature[j][8][1]]
                                            + integral_img[feature[j][9][0], feature[j][9][1]])
        if (classifier_value/2.0)/(feature[j][10]*1.0) < theta:
            img_i_detection_array.append(1)
            #sum_array[j] = sum_array[j] + 1
        else:
            img_i_detection_array.append(-1)
            #sum_array[j] = sum_array[j] - 1
    return img_i_detection_array#, sum_array


detection_array = []



img_path = 'C:/Users/100568635/Documents/GitHub/SOFE3720U/Face_Detection/img/exercise-5.jpg'
img = Image.open(img_path)
for resize_factor in xrange(min(img.width,img.height)/(window_size*2), 3, -1):
    img = Image.open(img_path)
    gray_img = img.convert(mode='L')
    Draw = ImageDraw.Draw(img)
    img_width = img.width / resize_factor
    img_height = img.height / resize_factor
    #img_height = 100
    #img_width = 100


    work_img = gray_img.resize((img_width, img_height))
    row = 0
    while (row + window_size) < img_height:
        row_shift =1
        column = 0
        while (column + window_size) < img_width:
            cropped_img = work_img.crop((row,column,row + window_size, column + window_size))
            img_array = np.asarray(cropped_img)
            integral_img = integral_img_from_array(img_array)

            img_i_detection_array = two_rectangles_values(integral_img)
            img_i_detection_array.extend(three_rectangles_values(integral_img))
            img_i_detection_array.extend(four_squares_values(integral_img))

            if np.sum(img_i_detection_array) > 110:
                Draw.rectangle([(column*resize_factor,row*resize_factor),((column+window_size)*resize_factor,(row+window_size)*resize_factor)])
                column += 1
                row_shift = 1
                #cropped_img.save('C:/Users/100568635/Documents/GitHub/SOFE3720U/Face_Detection/img/exercise-4_' + str(row) + '_' + str(column) + '.jpg')
            column += 1
        row += row_shift
    img.save(img_path + '_detected_' + str(resize_factor) + '.jpg')

    end_time = datetime.datetime.now()
    print end_time
    print end_time - start_time

