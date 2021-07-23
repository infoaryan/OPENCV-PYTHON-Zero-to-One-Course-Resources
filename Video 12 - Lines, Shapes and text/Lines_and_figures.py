import cv2
import numpy as np

#Creating a canvas 500X500 (Three channels)
canvas = np.zeros((500,500,3))

#Drawing a line
cv2.line(canvas, (0,0), (100,100), (0,255,0),2, cv2.LINE_4)
#line 4 and lin 8 - bresenham algo
#line AA - Gausian filtering
#Drawing a rectangle
cv2.rectangle(canvas, (200,200), (250,270),(0,0,255),-1)
#Drawing a Circle

cv2.circle(canvas, (250,250), 10, (255,0,0),3)
#Drawing a Arrowed line

cv2.arrowedLine(canvas, (400,400), (400,500), (255,255,255), tipLength=0.3)

#Showing the canvas
cv2.imshow('winname', canvas)
cv2.waitKey(20000)