import cv2 as cv
import numpy as np

src = cv.imread("E:\p1.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
'''
blur_op = np.ones([5, 5], dtype=np.float32)/25.
shape_op = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], np.float32)
grad_op = np.array([[1, 0],[0, -1]], dtype=np.float32)

dst1 = cv.filter2D(src, -1, blur_op)
dst2 = cv.filter2D(src, -1, shape_op)
dst3 = cv.filter2D(src, cv.CV_32F, grad_op)
dst3 = cv.convertScaleAbs(dst3)

cv.imshow("blur=5x5", dst1);
cv.imshow("shape=3x3", dst2);
cv.imshow("gradient=2x2", dst3);
'''
'''
x = cv.Sobel(src, cv.CV_16S, 1, 0)
y = cv.Sobel(src, cv.CV_16S, 0, 1)
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y) #转回uint8
dst = cv.addWeighted(absX, 0.5, absY, 0.5, 0) #组合起来
#dst = cv2.Sobel(src, ddepth图像的深度012, dx求导的阶数, dy求导的阶数[, dst[, ksize算子的大小[, scale[, delta[, borderType]]]]])
'''
dst = cv.Laplacian(src, cv.CV_32F, ksize=3, delta=127)#拉普拉斯算子
dst = cv.convertScaleAbs(dst)

cv.imshow('ss',dst)
cv.waitKey(0)
cv.destroyAllWindows()