import cv2 as cv
import numpy as np


def clamp(pv):
    if pv >255:
        pv = 255
    elif pv < 0 :
        pv = 0
    else:
        return pv
def gaussian_noise(image):  #对图像加上高斯噪声
    h,w,c = image.shape
    for row in range(h):#十分耗时
        for col in range(w):
            s = np.random.normal(0,20,3)#产生3个随机值，符合正态分布，第一个参数是概率分布的均值，对应分布中心，，第二个是概率分布的标准差，越小越瘦高，第三个是输出的值个数
            b = image[row,col,0] #blue
            g = image[row,col,1] #green
            r = image[row,col,2] #red
            image[row,col,0] = clamp(b+s[0])#为什么像素值是整数的怎么会和float相加呢？
            image[row,col,1] = clamp(g+s[1])
            image[row,col,2] = clamp(r+s[2])

    cv.imshow("noise image",image)

src = cv.imread("1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
gaussian_noise(src)
print(np.random.normal(0,20,3))

cv.waitKey(0)
cv.destroyAllWindows()
