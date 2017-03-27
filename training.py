from PIL import Image
import numpy as np
import os
# read pixels
# for 19 * 19 picture = 361 pixels
# multiply each pixel by position value
# values from 0 to 184110
# Max sum of values = 33323910
pixels_size = 19 * 19
multiplier_step = 2
multiplier_array = np.arange(2,(pixels_size * multiplier_step) + 1,multiplier_step)
# rotate every 19 pixels
#multiplier_array = (multiplier_array - 1) % 19

black_img = np.full(1,255,np.uint64)
max_value = np.sum(black_img * multiplier_array)
print 'max = ' , max_value

def image_to_value(image_file):
    """
    :param image_file:
    :return: image value
    """
    img = Image.open(image_file)
    #img.load()
    img_array = np.asarray(img,np.uint64).flatten()
    low_values_indices = img_array > 128  # want to keep low pixels, dark
    high_values_indices = img_array < 128 # want to keep high pixels, light
    #img_array[low_values_indices] = 0  # All low values set to 0
    img_light_value = img_array
    img_light_value[high_values_indices] = 0
    img_light_value = img_light_value * multiplier_array
    img_light_value = int(np.sum(img_light_value))
    img_dark_value = img_array
    img_dark_value[low_values_indices] = 0
    img_dark_value = img_dark_value * multiplier_array
    img_dark_value = int(np.sum(img_dark_value))
    img_array_value = [img_light_value,img_dark_value]

    #img_array = img_array * img_array
    #img_array = img_array  * multiplier_array
    #img_array = img_array * img_array
    #img_array = (img_array * multiplier_array - 170) % 170
    #img_array = img_array * img_array
    #sum
    #img_array_value = int(np.sum(img_array))
    # save the value
    return img_array_value
'''
def image_to_value_array(image_path):
    """
    :param image_path:
    :return: image value array
    """
    img = Image.open(image_path)
    #img.load()
    img_array = np.asarray(img,np.uint64).flatten()


    low_values_indices = img_array > 80  # Where values are low
    img_array[low_values_indices] = 0  # All low values set to 0


    #img_array = img_array * multiplier_array
    #img_array = img_array + 1
    #img_array = (img_array - 170) % 170
    img_array = img_array * img_array
    #sum
    #img_array_value = int(np.sum(img_array))
    # save the value
    return img_array
'''
def train(relative_path, save_path):
    """
    :param relative_path:path of source images
    :param save_path: path + filename to save the values
    :return: none
    """
    with open(save_path,'w+') as save_file:
        value_array = np.empty([2],dtype=np.uint64)
        for img in os.listdir(relative_path):

            value = image_to_value(str(relative_path+'/'+img))
            value = np.reshape(value,[2])
            value_array = np.append(value_array,value)
        value_array = np.delete(value_array,0,0)
        value_array = np.delete(value_array, 0, 0)
        value_array = np.reshape(value_array,[2,-1])
        np.savetxt(save_file,value_array,delimiter=',',newline='\n')
            #save_file.write(str(value)+ '\n')
'''
def train_array(relative_path,save_path):
    """
    :param relative_path:path of source images
    :param save_path: path + filename to save the values
    :return: none
    """
    with open(save_path,'w+') as save_file:
        value_array = np.empty([1,361],dtype=np.uint64)
        for img in os.listdir(relative_path):
            value_array = np.append(value_array, np.reshape(image_to_value_array(str(relative_path+'/'+img)),[1,361]),axis=0)
            #save_file.write(str(value_array)+ '\n')
        value_array = np.delete(value_array,0,0)
        np.savetxt(save_file,value_array,delimiter=',',newline='\n')
'''

train('train/face','train/images_values/face_values.txt')
train('train/non-face','train/images_values/non-face_values.txt')
