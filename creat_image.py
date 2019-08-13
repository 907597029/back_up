import cv2 as cv
import numpy as np

def creat_image():
    # image = np.zeros([400,400,3],np.uint8)
    # image[:,:,2]=np.ones([400,400])*255
    # cv.imshow("",image)

    # img = np.ones([400, 400, 3], np.uint8)
    # img = img *127#灰色
    # cv.imshow("creat image", img)
    # cv.imwrite("D:/image.jpg",img)

    img = np.zeros([4,4],np.uint8)
    img.fill(4066666.666)

    img = img.reshape([2,8])
    print(img)


src = cv.imread("1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
creat_image()
cv.waitKey(0)
cv.destroyAllWindows()
