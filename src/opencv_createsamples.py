import os

positive_images_path = '../face.train/train/face/'
negative_images_path = '../face.train/train/non-face/'
'''
with open('../face.train/train/info.dat','w+') as info_dat:
    for fileName in os.listdir(positive_images_path):
        img_info = 'face/' + fileName + ' 1 0 0 19 19\n'
        info_dat.writelines(img_info)
'''

with open('../face.train/train/bg.txt','w+') as bg:
    for fileName in os.listdir(negative_images_path):
        img_info = 'non-face/' + fileName + '\n'
        bg.writelines(img_info)