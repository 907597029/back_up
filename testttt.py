import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]  #宽
    width = image.shape[1]#高
    channels = image.shape[2]#通道数
    print("width:%s,height:%s,channels:%s"%(height,width,channels))
    #曝光
    for row in range(height):
        for col in range(width):
            for c in  range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixels_demo",image)


def access_pixels2(image):
    #曝光
    image = 255-image
    cv.imshow("pixels_demo2",image)


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse",dst)

def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret , frame = capture.read()
        if ret==False:
            cv.destroyAllWindows()
            break
        cv.imshow("video",frame)
        c = cv.waitKey(0)
        if c ==27:
            break


def get_image_info(image):
    print(type(image)) #数据类型
    print(image.shape) #宽=331，高=480，通道数=3 BGR
    print(image.size) #文件大小 331*480*3=476640
    print(image.dtype) #保存的格式 u int8
    pixel_data = np.array(image) #numpy保存的image数组
    print(pixel_data)
    print(image)

src = cv.imread("1.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
video_demo()
# get_image_info(src)
# t1 = cv.getTickCount()#getTickCount()：用于返回从操作系统启动到当前所经的计时周期数
# print("t1",t1)
# access_pixels2(src)
# t2 = cv.getTickCount()
# print("t2",t2)
# time = (t2-t1)/cv.getTickFrequency()#getTickFrequency()：用于返回CPU的频率。get Tick Frequency。这里的单位是秒，也就是一秒内重复的次数。
# print(t2-t1,time)
cv.waitKey(0)
cv.destroyAllWindows()
