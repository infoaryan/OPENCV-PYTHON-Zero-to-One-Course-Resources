import cv2
import numpy

#Loading image from memory
image = cv2.imread('nature.jpg')

#Translation matrix
matrix = numpy.float32([[1,0,100],[0,1,100]])

#Applying the matrix to the image 
translated = cv2.warpAffine(image, matrix, (image.shape[1]+100,image.shape[0]+100))

#Showing the image
cv2.imshow('translation', translated)
cv2.waitKey(4000)