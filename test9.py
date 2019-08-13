import cv2 as cv
import numpy as np

def video():
    capture = cv.VideoCapture(0)
    while(True):
        ret ,frame = capture.read()
        # frame = cv.flip(frame,1)
        if ret == False:
            break
        b, g, r = cv.split(frame) #分成三个bgr三个单通道的frame 但是为什么是灰色的
        cv.imshow("b",b)
        cv.imshow("g",g)
        cv.imshow("r",r)

        frame[:,:,0] = 0
        # frame[:, :, 1] = 0
        frame[:, :, 2] = 0
        cv.imshow("b=0", frame)#没有blue了
        src = cv.merge([b,g,r])#合并三个通道
        cv.imshow("changed image",src)#合并好了的图片
        c = cv.waitKey(50)
        if c == 27:
            cv.destroyAllWindows()
            break

video()