#Import go here
import cv2
import numpy as np

#Trackbar handler
def changeRadius(value):
	global radius
	radius = value
	

#For changing the focus of the mask 
def changeFocus(scope):
	global value
	value = scope

#Reading the image and getting properties
img = cv2.imread('test1.jpg')
rows, cols = img.shape[:2]
value = 1
radius = 130
mask = np.zeros((int(rows*(value*0.1+1)),int(cols*(value*0.1+1))))


cv2.namedWindow('Trackbars')
cv2.createTrackbar('Radius', 'Trackbars', 130, 500, changeRadius)
cv2.createTrackbar('Focus', 'Trackbars', 1, 10, changeFocus)

while(True):
	# generating vignette mask using Gaussian kernels
	kernel_x = cv2.getGaussianKernel(int(cols*(0.1*value+1)),radius)
	kernel_y = cv2.getGaussianKernel(int(rows*(0.1*value+1)),radius)
	kernel = kernel_y * kernel_x.T
	
	#Normalizing the kernel
	kernel = kernel/np.linalg.norm(kernel)	
	
	#Genrating a mask to image
	mask = 255 * kernel
	output = np.copy(img)
	# applying the mask to each channel in the input image
	mask_imposed = mask[int(0.1*value*rows):,int(0.1*value*cols):]
	for i in range(3):
		output[:,:,i] = output[:,:,i] * mask_imposed
	cv2.imshow('Original', img)
	cv2.imshow('Vignette', output)
	key = cv2.waitKey(50)
	if(key==ord('q')):
		break
	elif(key==ord('s')):
		cv2.imwrite('output_mask{}_deviation{}.jpg', output)




