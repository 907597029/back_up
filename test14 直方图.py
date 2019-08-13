import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_hist(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show("hist")


def image_hist(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()


def equalHist(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #全局均值化
    dst = cv.equalizeHist(gray)
    cv.imshow("equalizeHist",dst)

    #自适应直方图均衡化https://blog.csdn.net/kl1411/article/details/89100740
    clahe = cv.createCLAHE(clipLimit=5, tileGridSize=(3,3))
    dst = clahe.apply(gray)
    cv.imshow("clahe",dst)

def create_rgb_hist(image):
    h, w, c =image.shape
    rgbhist = np.zeros([16*16*16,1],np.float32)



src = cv.imread("6.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
# plot_hist(src)
# image_hist(src)
equalHist(src)
cv.waitKey(0)
cv.destroyAllWindows()