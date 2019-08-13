import cv2 as cv
import numpy as np

#算数运算
def add_demo(m1,m2):#加
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)

def subtract_demo(m1,m2):#减
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)


def multiply_demo(m1,m2):#乘
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)


def divide_demo(m1,m2):#除
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)


def others(m1,m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print("M1",M1)
    print("M2",M2)

    print("dev1",dev1)
    print("dev2",dev2)

    img = np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print("m",m)
    print("dev",dev)


#逻辑运算
def logic_demo(m1,m2):
    dst1 = cv.bitwise_and(m1, m2)
    dst2 = cv.bitwise_or(m1, m2)
    dst3 = cv.bitwise_not(m1)
    cv.imshow("logic_demo_and", dst1)
    cv.imshow("logic_demo_or", dst2)
    cv.imshow("logic_demo_not", dst3)


def contrast_bightness_demo(image,c,b):#c 对比度 b亮度
    h, w, ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c, blank, 1-c, b) #参数 第一张图 ， 第一章图的权重 ，  第二张图，第二章图的权重 ， 亮度
    cv.imshow("con-bri-demo",dst)



src1 = cv.imread("4.jpg")
src2 = cv.imread("5.jpg")
print(src1.shape)
print(src2.shape)
src3 = cv.imread("1.jpg")
cv.imshow("image",src3)
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
# cv.imshow("4",src1)
# cv.imshow("5",src2)
# add_demo(src1,src2)
# subtract_demo(src1,src2)
# multiply_demo(src1,src2)
# divide_demo(src1,src2)
# others(src1,src2)
# logic_demo(src1,src2)


contrast_bightness_demo(src3, 1.6, 25)#图 对比度， 亮度

cv.waitKey(0)
cv.destroyAllWindows()