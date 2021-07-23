#Import the required libraries
import cv2
import numpy as np


#Making a empty BLACK canvas
#Here canvas is of three layers
canvas = np.zeros((300,300,3))

#Required points we need to join
pts = np.array([[250, 5], [220, 80], [280, 80],[100,100],[250,250]], np.int32)

# Reshape the points to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))

# Draw this polygon 
#Here Boolean True and Flase determine if the figure is closed
cv2.polylines(canvas, [pts], True,(0,255,0), 3)


#Showing the canvas
cv2.imshow('winname', canvas)
cv2.waitKey(20000)