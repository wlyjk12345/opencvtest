import cv2 as cv
import numpy as np

src = cv.imread("E:\e/p2.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

# 提取划痕
mask = cv.inRange(hsv, (100, 43, 46), (124, 255, 255)) #通过不同的色彩值来分割图像
cv.imshow("mask", mask)
#cv.imwrite("mask.png", mask)

# 消除     图像修补的算法：1、基于快速行进算法 cv2.INPAINT_TELEA。2、基于流体动力学并使用了偏微分方程 cv2.INPAINT_NS。
se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
mask = cv.dilate(mask, se)  #修复掩膜
result = cv.inpaint(src, mask, 3, cv.INPAINT_TELEA)      # 3  修复区域的半径
cv.imshow("result", result)
#cv.imwrite("result.png", result)
cv.waitKey(0)