import cv2 as cv
from ultralytics import YOLO
import numpy as np
from weed import Weed
 
cap = cv.VideoCapture("test.mp4")
model = YOLO("this_is_it.pt")
 
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
 
while True :
    ret , frame = cap.read()

    if not ret :
        break

    frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
    frame = cv.resize(frame,(720,640))
    results = model(frame, stream=False)
    annotated_frame = results[0].plot()
    combined = np.hstack((frame, annotated_frame))
    combined = cv.resize(combined,(1440 , 640))

    Weed.getDetails(results[0],frame)

    cv.imshow("output" , combined)



    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()