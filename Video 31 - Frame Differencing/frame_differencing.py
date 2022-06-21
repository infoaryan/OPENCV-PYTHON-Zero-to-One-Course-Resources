import cv2
import numpy as np


kernel = np.ones((3,3))

# Compute the frame difference
def frame_diff(prev_frame, cur_frame, next_frame):
	diff_frames1 = cv2.absdiff(next_frame, cur_frame)
	# Absolute difference between current frame and previous frame
	diff_frames2 = cv2.absdiff(cur_frame, prev_frame)
	# Return the result of bitwise 'AND' between the above two resultant images
	return cv2.bitwise_and(diff_frames1, diff_frames2)

# Capture the frame from webcam
def get_frame(cap):
	ret, frame = cap.read()
	# Resize the image
	frame = cv2.resize(frame, None, fx=scaling_factor,
		fy=scaling_factor, interpolation=cv2.INTER_AREA)
	# Return the grayscale image
	return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

if __name__=='__main__':
	cap = cv2.VideoCapture(0)
	scaling_factor = 0.9
	prev_frame = get_frame(cap)
	cur_frame = get_frame(cap)
	next_frame = get_frame(cap)
	# Iterate until the user presses the ESC key
	while True:
		frame_difference = frame_diff(prev_frame,cur_frame, next_frame)
		#frame_difference = cv2.dilate(src, kernel)
		_,frame_th = cv2.threshold(frame_difference, 0, 255, cv2.THRESH_TRIANGLE)
		# frame_th = cv2.dilate(frame_th, kernel)
		cv2.imshow("Object Movement", frame_difference)
		cv2.imshow("Obje", frame_th)
		
		# Update the variables
		prev_frame = cur_frame
		cur_frame = next_frame
		next_frame = get_frame(cap)
		# Check if the user pressed ESC
		key = cv2.waitKey(5)
		if key == 27:
			break
	cv2.destroyAllWindows()