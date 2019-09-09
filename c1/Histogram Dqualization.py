import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def custom_hist(gray,n):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title(n)
    plt.show()


src = cv.imread("E:\k2.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.namedWindow("input", cv.WINDOW_NORMAL)
cv.imshow("input", gray)
dst = cv.equalizeHist(gray)    #void equalizeHist(InputArray src,OutputArray dst)   直方图均衡化，用于提高图像的质量；

cv.imshow("eh", dst)

custom_hist(gray,'1')
cv.waitKey(20)
custom_hist(dst,'2')

cv.waitKey(0)
cv.destroyAllWindows()