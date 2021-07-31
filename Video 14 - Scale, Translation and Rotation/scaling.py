import cv2
import numpy as np


#Scaling operation
#Reading original Image
image = cv2.imread('small.jpg')

image_sized = cv2.resize(image, (300,300))

#Resizing image using Linear interpolation
image_re_linear = cv2.resize(image, None, fx=5.5,fy=5.5, interpolation=cv2.INTER_LINEAR)

#Resizing using Cubic interpolation
image_re_cubic = cv2.resize(image, None, fx=5.5,fy=5.5, interpolation=cv2.INTER_CUBIC)

#Showing all three images
cv2.imshow('Linear', image_re_linear)
cv2.imshow('Cbubic', image_re_cubic)
cv2.imshow('original', image)

if(cv2.waitKey()==ord('q')):
	cv2.destroyAllWindows()