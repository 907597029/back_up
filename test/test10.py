import numpy as np
import cv2 as cv

def pyramid_demo(image):
    level=3
    temp =image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down"+str(i),dst)
        temp =dst.copy()
    return  pyramid_images


src = cv.imread("1.jpg")
cv.namedWindow("demo",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)
pyramid_demo(src)
cv.waitKey(0)
