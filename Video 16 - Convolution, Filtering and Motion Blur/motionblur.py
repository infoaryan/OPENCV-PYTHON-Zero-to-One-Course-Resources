import cv2
import numpy as np

img = cv2.imread('nature.jpg')
size = 15

kernel = np.zeros((size,size))
kernel[int((size-1)/2),:] = np.ones(size)
kernel = kernel/size

output  = cv2.filter2D(img, -1, kernel)
cv2.imshow('winname', output)
cv2.imshow('winnam1e', img)
cv2.waitKey(0)