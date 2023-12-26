import cv2

cam = cv2.VideoCapture(0)

while(True):
	ret, frame = cam.read()
	cv2.imshow("opencv", frame)
	if cv2.waitKey(10) == 27:
		break