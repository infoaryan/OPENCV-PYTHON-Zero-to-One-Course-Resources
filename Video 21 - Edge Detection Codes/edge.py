#import the dependencies
import cv2
import numpy as np


image = cv2.imread('test.jpg')
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# performing the edge detetcion
gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
gradients_sobely = cv2.Sobel(image, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

gradients_laplacian = cv2.Laplacian(image, -1)

canny_output = cv2.Canny(image, 80, 150)

cv2.imshow('Sobel x', gradients_sobelx)
cv2.imshow('Sobel y', gradients_sobely)
cv2.imshow('Sobel X+y', gradients_sobelxy)
cv2.imshow('laplacian', gradients_laplacian)
cv2.imshow('Canny', canny_output)
cv2.waitKey()
