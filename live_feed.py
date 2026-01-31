import cv2 as cv
from weed import Weed
 
cap = cv.VideoCapture("test.mp4")
 
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video file opened successfully!")
 
while True :
    ret , frame = cap.read()

    if not ret :
        print("Cannot get frame")
        break

    frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
    frame = cv.resize(frame,(640,420))

    cv.imshow ("Live Feed" , frame)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()