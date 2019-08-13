import cv2 as cv
import numpy as np


def color_shape_demo(image):
    gary = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gary",gary)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("HSV",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb",ycrcb)



src = cv.imread("1.jpg")
cv.namedWindow("demo",cv.WINDOW_AUTOSIZE)
cv.imshow("demo",src)
color_shape_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()