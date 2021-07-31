import cv2
import numpy

#Loading image from memory
image = cv2.imread('nature.jpg')

height, width = image.shape[:2]

#Translation matrix
matrix = cv2.getRotationMatrix2D((width/2,height/2), 10, 1)

#Applying the matrix to the image 
translated = cv2.warpAffine(image, matrix, (width, height))

#Showing the image
cv2.imshow('translation', translated)
cv2.waitKey(4000)