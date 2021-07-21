#Importing teh library
import cv2

#getting teh image from system
# The image has to be stored at same location as file
#By default it reads image in BGR format
image = cv2.imread('test.jpg')

#To read image in grayscale format 
image_gray = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)

#To read images as it is (With alha mask or something else)
image_as = cv2.imread('tes.jpg',cv2.IMREAD_UNCHANGED)


#To display teh image
cv2.imshow('window name', image)
cv2.imshow('Grayscale image', image_gray)
cv2.imshow('Unchanged iamge', image_as)

#Now we have to hold above created windows other wise program will end
#The parameter passed is Time in milliseconds
cv2.waitKey(5000)

cv2.destroyAllWindows()
