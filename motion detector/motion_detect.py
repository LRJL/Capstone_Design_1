#KHU CAPSTONE DESIGN PROJECT 2020-1 LRJL
#TEST SAMPLE CODE FOR MOTION DETECTION, TRACKING

#code cited from
#https://www.youtube.com/watch?v=MkcUgPhOlP8

from cv2 import cv2
import numpy as np

#retrieve test clip
cap = cv2.VideoCapture('test.mp4')

#capture two frames
rval, frame1 = cap.read()
rval, frame2 = cap.read()

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)  #difference of two frames
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)    #convert diff into greyscale

    blur = cv2.GaussianBlur(gray, (5,5), 0) #blur image to reduce noise
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #set threshold
    dilated = cv2.dilate(thresh, None, iterations=3) #fill holes in the thresholded image
    
    #find contour
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #further implementation(removing, rectangle)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)    #values of contour

        if cv2.contourArea(contour) < 45000:    #to remove small unnecessary contours, (modify number)
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)   #draw rectangle on frame1
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3)  #put text on frame1


    #cv2.drawContours(frame1, contours, -1, (255, 0, 0), 2) #for runs without further implementation

    cv2.imshow("feed", frame1)  #show results
    
    #change to next frame
    frame1 = frame2 
    rval, frame2 = cap.read()

    #incase of error
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()