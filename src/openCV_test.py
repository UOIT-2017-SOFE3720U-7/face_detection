import numpy as np
import cv2
from PIL import Image
import os

face_cascade_path = os.path.abspath('train/cascade_ALL_HAAR/Group7_cascade_face_ALL_HAAR.xml')
img_path = 'img/exercise-5.jpg'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
#eye_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_eye.xml')

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    #for (ex,ey,ew,eh) in eyes:
    #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imwrite('img/detected.png',img)

cv2.imshow('image',img)
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.waitKey(0)
cv2.destroyAllWindows()
