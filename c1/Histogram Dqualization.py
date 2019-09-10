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
           #  x  ,y
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title(n)
    plt.show()


src = cv.imread("E:\k2.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.namedWindow("input", cv.WINDOW_NORMAL)
cv.imshow("input", gray)
dst = cv.equalizeHist(gray)    #void equalizeHist(InputArray src,OutputArray dst)   直方图均衡化，用于提高图像的质量；
cv.normalize(gray, gray, 0, 256, cv.NORM_MINMAX) #void normalize(InputArray src, OutputArray dst, double alpha=1, double beta=0, int norm_type=NORM_L2, int dtype=-1, InputArray mask=noArray() )
                                                 #归一化函数                                       模式的最小值     模式的最大值    NORM_MINMAX:数组的数值被平移或缩放到一个指定的范围


cv.imshow("dst", dst)
cv.imshow("nor", gray)

custom_hist(gray,'1')
cv.waitKey(20)
custom_hist(dst,'2')

methods = [cv.HISTCMP_CORREL, cv.HISTCMP_CHISQR,         #相关性比较 (method=cv.HISTCMP_CORREL)越大，相关度越高  卡方比较(method=cv.HISTCMP_CHISQR 值越小，相关度越高
           cv.HISTCMP_INTERSECT, cv.HISTCMP_BHATTACHARYYA]# 巴氏距离比较(method=cv.HISTCMP_BHATTACHARYYA) 值越小，相关度越高
str_method = ""
for method in methods:
    src1_src2 = cv.compareHist(gray, dst, method)
    print(src1_src2)

cv.waitKey(0)
cv.destroyAllWindows()