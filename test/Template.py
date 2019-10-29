import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import STANDERD

img = cv.imread("E:\k2.jpg",cv.IMREAD_COLOR)
cv.namedWindow("result",cv.WINDOW_NORMAL)

# 预处理
shape_op = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], np.float32)
img = cv.filter2D(img, -1, shape_op)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, binary= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
t = cv.medianBlur(binary, 5)
height, width = img.shape[:2]
# 边
edges = cv.Canny((t),1,10)
contours1, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    area = cv.contourArea(contours[c]) # 计算面积
    x, y, w, h = cv.boundingRect(contours[c]);
    arclen = cv.arcLength(contours[c], True)  # 计算弧长， True表示闭合区域
    if h > (height//2):
        continue
    if area < 150 or arclen < 150:
        continue
    cv.drawContours(binary, contours, c, (0), 2, 8)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 1, 8, 0);
    cv.putText(img, "bad", (x, y - 2), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 2)

cv.drawContours(img,contours1,-1,color = (0, 255, 255),thickness = -1)
cv.imshow('d',img)

# 成图
result = STANDERD.result_out(gray, edges, t)

# 记录出图
#STANDERD.outdraw(result)
cv.imwrite("binary.png", img)
cv.imshow("result", result)

#  阈值测试 STANDER.py
STANDERD.thre(binary,img)

k = cv.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()