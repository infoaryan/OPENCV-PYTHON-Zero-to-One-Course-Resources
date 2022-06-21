import cv2
import numpy

#Read the image and convert it to grayscale
image = cv2.imread('pexels-photo-569986.png')
image = cv2.resize(image, None, fx=0.9,fy=0.9)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Now convert the grayscale image to binary image
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Now detect the contours
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

#Visualize the data structure
print("Length of contours {}".format(len(contours)))
print(contours)

# draw contours on the original image
image_copy = image.copy()
image_copy = cv2.drawContours(image_copy, contours, -1, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

#Visualizing the results
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Drawn Contours', image_copy)
cv2.imshow('Binary Image', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()


