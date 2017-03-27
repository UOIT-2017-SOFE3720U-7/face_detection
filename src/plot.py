import matplotlib.pyplot as plt
import numpy as np

positives_file_path = '..//train//images_values//face_values.txt'
negatives_file_path = '..//train//images_values//non-face_values.txt'

with open(positives_file_path) as positives_file:
    #positive_values_array = np.empty([1,361])
#positive_values_array = np.loadtxt(positives_file_path,delimiter=',')
    #positive_values_array = np.fromfile(positives_file,int,-1)

    #positive_values = np.fromfile(positives_file,np.uint64,-1,'\n')
    positive_values = np.loadtxt(positives_file_path,delimiter=',')
#with open(negatives_file_path) as negatives_file:

#negative_values_array = np.loadtxt(negatives_file_path,delimiter=',')
    #negative_values_array = np.fromfile(negatives_file, int, -1)

#with open(negatives_file_path) as negatives_file:
    #negative_values = np.fromfile(negatives_file, np.uint64, -1, '\n')
    negative_values=np.loadtxt(negatives_file_path,delimiter=',')

'''
for values in positive_values_array:
    plt.plot(np.arange(0,361),values,'go')
for values in negative_values_array:
    plt.plot(np.arange(0,361),values,'ro')
'''

plt.plot(positive_values[[0]],positive_values[[1]], 'go')
plt.plot(negative_values[[0]],negative_values[[1]], 'ro')
plt.title('positive & negative values')
#plt.ylabel("Fitness Error")
#plt.xlabel("NFC")
plt.yscale('log')
#plt.savefig("../img/all_runs/" + algo + "_" + str(fn) + "_" + str(D) + ".png", bbox_inches='tight')
#plt.close()
plt.show()