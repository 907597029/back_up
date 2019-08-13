import cv2 as cv
import numpy as np

def video():
    capture = cv.VideoCapture(0)
    while(True):
        ret ,frame = capture.read()
        frame = cv.flip(frame,1)
        # frame = cv.blur(frame,(8,8))#均值模糊
        # frame = cv.medianBlur(frame, 9)  # 中值模糊
        # frame = cv.GaussianBlur(frame,(9,9),0)# 高斯模糊
        # frame = cv.bilateralFilter(frame, 0, 100, 15)  # 高斯双边
        frame = cv.pyrMeanShiftFiltering(frame, 10, 50)#均值迁移
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