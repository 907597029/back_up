import cv2 as cv
import numpy as np

#均值模糊 可以去噪声
def blur_demo(image):
    dst = cv.blur(image, (1, 9))
    cv.imshow("blur_demo", dst)

#中值模糊 可以去掉椒盐噪声
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)

#自定义模糊
def custom_blur_demo(image):
    kernel = np.ones([5, 5], np.float32)/25
    print(kernel)
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo", dst)

#自定义模糊 锐化 卷积核的值加起来为0 或1
def custom_blur_demo_ruihua(image):
    kernel = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]],np.float32)/9
    print(kernel)
    dst = cv.filter2D(image, -1, kernel=kernel)#ddepth=-1 这个是深度 一般为-1
    cv.imshow("custom_blur_demo_ruihua", dst)

src = cv.imread("6.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# blur_demo(src)
# median_blur_demo(src)
# custom_blur_demo(src)
custom_blur_demo_ruihua(src)
cv.waitKey(0)
cv.destroyAllWindows()
