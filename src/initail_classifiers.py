import numpy as np
from integral_image import *
import Haar_features
import os
import datetime
import pickle

# 2 squares value = sign * (A - B -2C + 2D + E - F)
# 3 squares value = sign * (A - B - 2C + 2D + H - G + 2E - 2F )
# 4 squares value = sign * (A - 2B + C - 2D + 4E - 2F + G - 2H + I

start_time = datetime.datetime.now()
print start_time
#theta = -5
window_size = 19
for theta in xrange(-19, 0, 1):

    print '###############################################################'
    print 'theta = ', str(theta)
    #weak_classifiers = Haar_features.all_features(19)
    two_rectangles = Haar_features.two_rectangles(window_size)
    three_rectangles = Haar_features.three_rectangles(window_size)
    four_squares = Haar_features.four_squares(window_size)


    # Start of features valuation
    #################################################################
    def two_rectangles_values(integral_img, sum_array, sample_type=1):
        img_i_detection_array=[]
        #sum_array_len = len(sum_array)
        for j in xrange(0, len(two_rectangles)):
            feature = two_rectangles
            # 2 squares value = sign * (A - B -2C + 2D + E - F)
            classifier_value = sample_type * feature[j][0] * (integral_img[feature[j][1][0], feature[j][1][1]] -
                                                              integral_img[feature[j][2][0], feature[j][2][1]] -
                                                              2 * integral_img[feature[j][3][0], feature[j][3][1]] +
                                                              2 * integral_img[feature[j][4][0], feature[j][4][1]] +
                                                              integral_img[feature[j][5][0], feature[j][5][1]] -
                                                              integral_img[feature[j][6][0], feature[j][6][1]])
            if classifier_value/(feature[j][7]*1.0) < theta:
                #img_i_detection_array.append(1)
                sum_array[j] = sum_array[j] + 1
            else:
                #img_i_detection_array.append(-1)
                sum_array[j] = sum_array[j] - 1
        return img_i_detection_array, sum_array


    def three_rectangles_values(integral_img, sum_array, sample_type=1):
        img_i_detection_array = []
        #sum_array_len = len(sum_array)
        for j in xrange(0, len(three_rectangles)):
            feature = three_rectangles
            # 3 squares value = sign * (A - B - 2C + 2D + 2E - 2F - G + H)
            # new equation: value = sing * (((A - B - C + D + E - F - G + H)/2.0) - (C - D - E + F))
            classifier_value = sample_type * feature[j][0] * (((integral_img[feature[j][1][0], feature[j][1][1]]
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
                #img_i_detection_array.append(1)
                sum_array[j] = sum_array[j] + 1
            else:
                #img_i_detection_array.append(-1)
                sum_array[j] = sum_array[j] - 1
        return img_i_detection_array, sum_array


    def four_squares_values(integral_img,sum_array, sample_type=1):
        img_i_detection_array = []
        #sum_array_len = len(sum_array)
        for j in xrange(0, len(four_squares)):
            feature = four_squares
            # 4 squares value = sign * (A - 2B + C - 2D + 4E - 2F + G - 2H + I
            classifier_value = sample_type * feature[j][0] * (integral_img[feature[j][1][0], feature[j][1][1]]
                                                - 2 * integral_img[feature[j][2][0], feature[j][2][1]]
                                                + integral_img[feature[j][3][0], feature[j][3][1]]
                                                - 2 * integral_img[feature[j][4][0], feature[j][4][1]]
                                                + 4 * integral_img[feature[j][5][0], feature[j][5][1]]
                                                - 2 * integral_img[feature[j][6][0], feature[j][6][1]]
                                                + integral_img[feature[j][7][0], feature[j][7][1]]
                                                - 2 * integral_img[feature[j][8][0], feature[j][8][1]]
                                                + integral_img[feature[j][9][0], feature[j][9][1]])
            if (classifier_value/2.0)/(feature[j][10]*1.0) < theta:
                #img_i_detection_array.append(1)
                sum_array[j] = sum_array[j] + 1
            else:
                #img_i_detection_array.append(-1)
                sum_array[j] = sum_array[j] - 1
        return img_i_detection_array, sum_array


    #detection_array = []
    positive_img_path = '../train/face/'
    negative_img_path = '../train/non-face/'
    # initial test
    detection_two_rectangles_sums_array = [0] * len(two_rectangles)
    detection_three_rectangles_sums_array= [0] * len(three_rectangles)
    detection_four_squares_sums_array = [0] * len(four_squares)

    print 'Face images'
    for img in os.listdir(positive_img_path):
        integral_img = integral_img_from_file(positive_img_path + img)
        # add row and column of zeros to integral image to have zero for negative indices
        integral_img = np.insert(integral_img, 19, [0], axis=1)
        integral_img = np.insert(integral_img, 19, [0], axis=0)
        #img_i_detection_array = []

        detection_two_rectangles_sums_array = two_rectangles_values(integral_img,detection_two_rectangles_sums_array, 1)[1]
        detection_three_rectangles_sums_array = three_rectangles_values(integral_img, detection_three_rectangles_sums_array, 1)[1]
        detection_four_squares_sums_array = four_squares_values(integral_img, detection_four_squares_sums_array, 1)[1]

        #detection_array.extend(img_i_detection_array)

    print 'Non-face images'
    for img in os.listdir(negative_img_path):
        integral_img = integral_img_from_file(negative_img_path + img)
        # add row and column of zeros to integral image to have zero for negative indices
        integral_img = np.insert(integral_img, 19, [0], axis=1)
        integral_img = np.insert(integral_img, 19, [0], axis=0)

        detection_two_rectangles_sums_array = two_rectangles_values(integral_img,detection_two_rectangles_sums_array, -1)[1]
        detection_three_rectangles_sums_array = three_rectangles_values(integral_img, detection_three_rectangles_sums_array, -1)[1]
        detection_four_squares_sums_array = four_squares_values(integral_img, detection_four_squares_sums_array, -1)[1]
        # End of features valuation
        #############################################################

    end_time = datetime.datetime.now()
    print end_time
    print end_time - start_time

    print 'len 2 sums = ',len(detection_two_rectangles_sums_array)
    print 'len 3 sums = ',len(detection_three_rectangles_sums_array)
    print 'len 4 sums = ', len(detection_four_squares_sums_array)

    print 'len 2 = ', len(two_rectangles)
    print 'len 3 = ', len(three_rectangles)
    print 'len 4 = ', len(four_squares)

    # filter features:
    for i in xrange(len(detection_two_rectangles_sums_array)):
        two_rectangles[i].append(detection_two_rectangles_sums_array[i])
    two_rectangles = [item[0:-1] for item in two_rectangles if item[-1] > 0]

    for i in xrange(len(detection_three_rectangles_sums_array)):
        three_rectangles[i].append(detection_three_rectangles_sums_array[i])
    three_rectangles = [item[0:-1] for item in three_rectangles if item[-1] > 0]

    for i in xrange(len(detection_four_squares_sums_array)):
        four_squares[i].append(detection_four_squares_sums_array[i])
    four_squares = [item[0:-1] for item in four_squares if item[-1] > 0]

    print 'new len'
    print 'len 2 = ', len(two_rectangles)
    print 'len 3 = ', len(three_rectangles)
    print 'len 4 = ', len(four_squares)

    print 'saving classifiers'

    #save classifiers to files:
    with open('two_rectangles_classifiers_' + str(abs(theta)),'w+') as f :
        pickle.dump(two_rectangles,f)
    with open('three_rectangles_classifiers_' + str(abs(theta)),'w+') as f:
        pickle.dump(three_rectangles,f)
    with open('four_squares_classifiers_' + str(abs(theta)),'w+') as f:
        pickle.dump(four_squares,f)

    print datetime.datetime.now()
    print datetime.datetime.now() - end_time
