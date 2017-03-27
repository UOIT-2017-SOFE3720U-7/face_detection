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
theta = -50
window_size = 19

#weak_classifiers = Haar_features.all_features(19)
with open('two_rectangles_classifiers') as f:
    two_rectangles = pickle.load(f)
with open('three_rectangles_classifiers') as f:
    three_rectangles = pickle.load(f)
with open('four_squares_classifiers') as f:
    four_squares = pickle.load(f)




# Start of features valuation
#################################################################
def two_rectangles_values(integral_img, sum_array, weight, sample_type=1):
    sum_of_votes = 0
    for j in xrange(0, len(two_rectangles)):
        feature = two_rectangles
        # 2 squares value = sign * (A - B -2C + 2D + E - F)
        classifier_value = sample_type * feature[j][0] * (integral_img[feature[j][1][0], feature[j][1][1]] -
                                                          integral_img[feature[j][2][0], feature[j][2][1]] -
                                                          2 * integral_img[feature[j][3][0], feature[j][3][1]] +
                                                          2 * integral_img[feature[j][4][0], feature[j][4][1]] +
                                                          integral_img[feature[j][5][0], feature[j][5][1]] -
                                                          integral_img[feature[j][6][0], feature[j][6][1]])

        if classifier_value < theta:
            sum_of_votes = sum_of_votes + (1 * weight)
            sum_array[j] = sum_array[j] + 1
        else:
            sum_of_votes = sum_of_votes - 1
            sum_array[j] = sum_array[j] - (1 * weight)
    return sum_of_votes, sum_array


def three_rectangles_values(integral_img, sum_array, weight, sample_type=1):
    sum_of_votes = 0
    for j in xrange(0, len(three_rectangles)):
        feature = three_rectangles
        # 3 squares value = sign * (A - B - 2C + 2D + 2E - 2F - G + H)
        classifier_value = sample_type * feature[j][0] * (integral_img[feature[j][1][0], feature[j][1][1]]
                                                          - integral_img[feature[j][2][0], feature[j][2][1]]
                                                          - 2 * integral_img[feature[j][3][0], feature[j][3][1]]
                                                          + 2 * integral_img[feature[j][4][0], feature[j][4][1]]
                                                          + 2 * integral_img[feature[j][5][0], feature[j][5][1]]
                                                          - 2 * integral_img[feature[j][6][0], feature[j][6][1]]
                                                          - integral_img[feature[j][7][0], feature[j][7][1]]
                                                          + integral_img[feature[j][8][0], feature[j][8][1]])
        if classifier_value < theta:
            sum_of_votes = sum_of_votes + (1 * weight)
            sum_array[j] = sum_array[j] + 1
        else:
            sum_of_votes = sum_of_votes - 1
            sum_array[j] = sum_array[j] - (1 * weight)
    return sum_of_votes, sum_array


def four_squares_values(integral_img,sum_array, weight, sample_type=1):
    sum_of_votes = 0
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
        if classifier_value < theta:
            sum_of_votes = sum_of_votes + 1
            sum_array[j] = sum_array[j] + (1 * weight)
        else:
            sum_of_votes = sum_of_votes - 1
            sum_array[j] = sum_array[j] - (1 * weight)
    return sum_of_votes, sum_array



positive_img_path = '../train/face/'
negative_img_path = '../train/non-face/'
weight = [1] * (len(os.listdir(positive_img_path))+ len(os.listdir(negative_img_path)))

detection_two_rectangles_sums_array = [0] * len(two_rectangles)
detection_three_rectangles_sums_array= [0] * len(three_rectangles)
detection_four_squares_sums_array = [0] * len(four_squares)

vote = []

print 'Face images'
for img in os.listdir(positive_img_path):
    vote.append(0)
    integral_img = integral_img_from_file(positive_img_path + img)
    # add row and column of zeros to integral image to have zero for negative indices
    integral_img = np.insert(integral_img, 19, [0], axis=1)
    integral_img = np.insert(integral_img, 19, [0], axis=0)
    #img_i_detection_array = []

    sum_2, detection_two_rectangles_sums_array = two_rectangles_values(integral_img,detection_two_rectangles_sums_array, weight[len(vote)-1], 1)
    sum_3, detection_three_rectangles_sums_array = three_rectangles_values(integral_img, detection_three_rectangles_sums_array, weight[len(vote)-1], 1)
    sum_4, detection_four_squares_sums_array = four_squares_values(integral_img, detection_four_squares_sums_array, weight[len(vote)-1], 1)
    vote[-1] = sum_2 + sum_3 + sum_4

    #detection_array.extend(img_i_detection_array)

print 'Non-face images'
for img in os.listdir(negative_img_path):
    vote.append(0)
    integral_img = integral_img_from_file(negative_img_path + img)
    # add row and column of zeros to integral image to have zero for negative indices
    integral_img = np.insert(integral_img, 19, [0], axis=1)
    integral_img = np.insert(integral_img, 19, [0], axis=0)

    sum_2, detection_two_rectangles_sums_array = two_rectangles_values(integral_img,detection_two_rectangles_sums_array, weight[len(vote)-1], -1)
    sum_3, detection_three_rectangles_sums_array = three_rectangles_values(integral_img, detection_three_rectangles_sums_array, weight[len(vote)-1], -1)
    sum_4, detection_four_squares_sums_array = four_squares_values(integral_img, detection_four_squares_sums_array, weight[len(vote)-1], -1)
    vote[-1] = sum_2 + sum_3 + sum_4
    # End of features valuation
    #############################################################
# assign new weight



for i in xrange(len(vote)):
    if vote[i] < 1:
        weight[i] = 2
    else:
        weight[i] = 1

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


print 'saving votes'

#save classifiers to files:
with open('vote','w+') as f :
    pickle.dump(vote,f)

print datetime.datetime.now()
print datetime.datetime.now() - end_time
print 'end'