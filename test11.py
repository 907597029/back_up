import cv2 as cv
import numpy as np


def fill_color_demo(image):
    pass

src = cv.imread("1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

face = src[50:200,100:200]# 高 宽
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[50:200,100:200]= backface
cv.imshow("face",src)


cv.waitKey(0)
cv.destroyAllWindows()
