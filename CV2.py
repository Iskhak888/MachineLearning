import cv2
image = cv2.imread("C:\\Users\\iskha\Downloads\\100_0140\\100_0140\\DJI_0001.JPG")
if image is None:
    print ("Error reading image")
else:
    cv2.imshow("My Image", image)
    cv2.waitkey(0)
    cv2.destroyAllWindows()