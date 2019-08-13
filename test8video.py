import cv2 as cv
import numpy as np

def video():
    capture = cv.VideoCapture(0)
    while(True):
        ret ,frame = capture.read()
        frame = cv.flip(frame,1)
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 43, 46])
        upper_hsv = np.array([10, 255, 255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c = cv.waitKey(50)
        if c == 27:
            cv.destroyAllWindows()
            break

video()