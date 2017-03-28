import numpy as np
from integral_image import *
import Haar_features
import os
import datetime
import pickle
from math import *

# 2 squares value = sign * (A - B -2C + 2D + E - F)
# 3 squares value = sign * (A - B - 2C + 2D + H - G + 2E - 2F )
# 4 squares value = sign * (A - 2B + C - 2D + 4E - 2F + G - 2H + I

start_time = datetime.datetime.now()
print start_time

window_size = 19
polarity = 1
threshold = 0
print 'window size = ', window_size
print 'polarity = ' , polarity
print 'threshold =', threshold
# construct features
features = Haar_features.all_features(window_size)

print 'features constructed'

positive_img_path = '../train/face/'
negative_img_path = '../train/non-face/'
number_positive_images = len(os.listdir(positive_img_path))
number_negative_images = len(os.listdir(negative_img_path))
# initial weights
p_init_weight = 1.0/(2*number_positive_images)
n_init_weight = 1.0/(2*number_negative_images)

integral_img_list  = []



# load imges
# convert images into integral images
# add weight and type of image (p, n) to integral images
#
# integral_img_list :
# [][0] : integral image
# [][1] : type
# [][2] : weight
# [][3] : > 0, classified correctly
for img in os.listdir(positive_img_path):
    integral_img_list.append([integral_img_from_file(positive_img_path + img),1,p_init_weight,0])
print 'positive images loaded and weighted'
for img in os.listdir(negative_img_path):
    integral_img_list.append([integral_img_from_file(negative_img_path + img),0,n_init_weight,0])
print 'negative images loaded and weighted'

print 'selecting classifiers'
T = 20
selected_feature = []
for t in xrange(1, T):
    weights_sum = np.sum(integral_img_list,axis=0)[2]
    # normalize weight
    for integral_img in integral_img_list:
        integral_img[2] = integral_img[2]/weights_sum
    # select best weak classifier with respect to the weighted error
    min_sum_error = 1

    for i in xrange(0,len(features)):
        feature = features[i]
        errors_sum = 0
        for integral_img in integral_img_list:
            error = Haar_features.feature_error(feature,integral_img[0],integral_img[2],integral_img[1],polarity,threshold)
            # was the image classified correctly?
            if error > 0:
                integral_img[3] += 1
            else:
                integral_img[3] -= 1
            errors_sum = errors_sum + error

        if errors_sum < min_sum_error:
            min_sum_error = errors_sum
            feature_index = i


    beta = min_sum_error/(1-min_sum_error)
    # save best feature
    alpha = log10(1/beta)
    selected_feature.append([features[feature_index], alpha])
    del features[feature_index]
    print 'classifier ' + str(T) + ' selected'
    print 'beta = ', str(beta)
    print 'alpha = ', str(alpha)

    # update weights
    for img in integral_img_list:
        if img[3] > 0:
            e = 0
        else:
            e = 1
        new_weight = img[2] * pow(beta, (1-e))
        img[2] = new_weight

    with open('selected_classifier_' + str(t), 'w+') as f:
        pickle.dump(selected_feature, f)
    with open('remaining_classifiers', 'w+') as f:
        pickle.dump(features, f)
    end_time = datetime.datetime.now()
    print end_time
    print (end_time - start_time)
