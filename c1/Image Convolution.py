import cv2 as cv
import numpy as np


def custom_blur(src):
    h, w, ch = src.shape
    print("h , w, ch", h, w, ch)
    result = np.copy(src)
    for row in range(1, h-1, 1):
        for col in range(1, w-1, 1):
            v1 = np.int32(src[row-1, col-1])              #3X3空间像素平均
            v2 = np.int32(src[row-1, col])
            v3 = np.int32(src[row-1, col+1])
            v4 = np.int32(src[row, col-1])
            v5 = np.int32(src[row, col])
            v6 = np.int32(src[row, col+1])
            v7 = np.int32(src[row+1, col-1])
            v8 = np.int32(src[row+1, col])
            v9 = np.int32(src[row+1, col+1])

            b = v1[0] + v2[0] + v3[0] + v4[0] + v5[0] + v6[0] + v7[0] + v8[0] + v9[0];
            g = v1[1] + v2[1] + v3[1] + v4[1] + v5[1] + v6[1] + v7[1] + v8[1] + v9[1];
            r = v1[2] + v2[2] + v3[2] + v4[2] + v5[2] + v6[2] + v7[2] + v8[2] + v9[2];
            result[row, col] = [b//9, g//9, r//9]
    cv.imshow("result", result)


src = cv.imread("E:\p1.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
dst = cv.blur(src, (3, 3))   #均值模糊（Averaging blurring  均值滤波是典型的线性滤波算法，它是指在图像上对目标像素给一个模板，该模板包括了其周围的临近像素（
                    #Size ksize内核的大小         #以目标像素为中心的周围8个像素，构成一个滤波模板，即去掉目标像素本身），再用模板中的全体像素的平均值来代替原来像素值。
cv.imshow("blur", dst)
custom_blur(src)

dst2 = cv.GaussianBlur(src, (5, 5), sigmaX=15)# void GaussianBlur(InputArray src, OutputArray dst, Size ksize, double sigmaX, double sigmaY=0, int borderType=BORDER_DEFAULT);
dst3 = cv.GaussianBlur(src, (0, 0), sigmaX=15)# ksize，高斯内核，sigmaX，表示高斯核函数在X方向的的标准偏差，borderType，用于推断图像外部像素的某种边界模式
dst5 = cv.medianBlur(src,5) #中值滤波
cv.imshow("gaussian ksize=5", dst2) #高斯滤波，高斯模糊
cv.imshow("gaussian sigmax=15", dst3)
cv.imshow("medianBlur",dst5)  #中值模糊
cv.waitKey(0)
cv.destroyAllWindows()