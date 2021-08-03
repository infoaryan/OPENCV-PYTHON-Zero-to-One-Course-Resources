#Getting the imports 
import cv2
import numpy as np

#Reading the image
img = cv2.imread('nature.jpg')

#Gauusian kernel for sharpening
gaussian_blur = cv2.GaussianBlur(img, (7,7), 2)

#Sharpening using addweighted()
sharpened1 = cv2.addWeighted(img,1.5, gaussian_blur, -0.5, 0)
sharpened2 = cv2.addWeighted(img,3.5, gaussian_blur, -2.5, 0)
sharpened3 = cv2.addWeighted(img,7.5, gaussian_blur, -6.5, 0)

#Showing the sharpened Images
cv2.imshow('Sharpened 3', sharpened3)
cv2.imshow('Sharpened 2', sharpened2)
cv2.imshow('Sharpened 1', sharpened1)
cv2.imshow('original', img)
cv2.waitKey(0)