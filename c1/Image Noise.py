import cv2 as cv
import numpy as np


def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=np.int)   # numpy.random.randint(low, high=None, size=None, dtype='l')
    cols = np.random.randint(0, w, nums, dtype=np.int)                                        # size : int or tuple of ints, optional 输出的大小，可以是整数，或者元组

    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image


def gaussian_noise(image):
    noise = np.zeros(image.shape, image.dtype)
    m = (15, 15, 15)
    s = (30, 30, 30)
    cv.randn(noise, m, s)  #以给定的形状创建一个数组，数组元素来符合标准正态分布N(0,1)
    dst = cv.add(image, noise)
    cv.imshow("gaussian noise", dst)
    return dst

'''
src = cv.imread("E:\p1.png")
h, w = src.shape[:2]
copy = np.copy(src)
gaussian_noise(src)
copy = add_salt_pepper_noise(copy)
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = copy
cv.putText(result, "original image", (10, 30), cv.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 255), 1)
cv.putText(result, "salt pepper image", (w+10, 30), cv.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 255), 1)
cv.imshow("salt pepper noise", result)
cv.imwrite("./result.png", result)

'''
src = cv.imread("E:\p1.png")
cv.imshow("input", src)
h, w = src.shape[:2]
src = gaussian_noise(src)
'''
result1 = cv.blur(src, (5, 5))
cv.imshow("result-1", result1)

result2 = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("result-2", result2)

result3 = cv.medianBlur(src, 5)
cv.imshow("result-3", result3)

result4 = cv.fastNlMeansDenoisingColored(src, None, 15, 15, 10, 30)   #从彩色图像中去除噪声    cv2.fastNlMeansDenoising() 使用对象为灰度图
cv.imshow("result-4", result4)
'''
dst = cv.bilateralFilter(src, 0, 100, 10)        #bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) #双边滤波
 #- d:   在过滤期间使用的每个像素邻域的直径 sigmaColor: 色彩空间的标准方差，一般尽可能大。sigmaSpace: 坐标空间的标准方差(像素单位)，一般尽可能小。
dst = cv.pyrMeanShiftFiltering(src, 15, 30, termcrit=(cv.TERM_CRITERIA_MAX_ITER+cv.TERM_CRITERIA_EPS, 5, 1))
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = dst
result = cv.resize(result, (w*2,h ))
cv.imshow("result", result)

cv.waitKey(0)
cv.destroyAllWindows()