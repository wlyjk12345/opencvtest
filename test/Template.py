import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
img = cv.imread("E:\p9.jpg",cv.IMREAD_COLOR)
cv.namedWindow("result",cv.WINDOW_NORMAL)
# 预处理
shape_op = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], np.float32)
img = cv.filter2D(img, -1, shape_op)
#img = cv.edgePreservingFilter(img, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)  #保边滤波器
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#gray= cv.medianBlur(gray, 9)
#result1 = cv.GaussianBlur(gray, (9, 9), 0)
binary =  gray
result1 = gray
#dst = cv.pyrMeanShiftFiltering(img, 15, 30, termcrit=(cv.TERM_CRITERIA_MAX_ITER+cv.TERM_CRITERIA_EPS, 5, 1))

#se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))# 顶帽操作
#binary = cv.morphologyEx(result1, cv.MORPH_BLACKHAT, se)
ret, th = cv.threshold(binary, 127, 255, cv.THRESH_BINARY)
#t= cv.GaussianBlur(th, (9, 9), 0)
t = cv.medianBlur(th, 5)
cv.imshow('d',t)
# 边缘
edges = cv.Canny((t),1,10)
'''
dst = cv.Laplacian(result1, cv.CV_32F, ksize=3, delta=127) #
img = cv.convertScaleAbs(dst)

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpen_image = cv.filter2D(dst, cv.CV_32F, sharpen_op)
sharpen_image = cv.convertScaleAbs(sharpen_image)
'''
#edges = cv.Canny((dst),1,10)
contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(t,contours,-1,color = (255, 255, 255),thickness = -1)

# 成图
h, w = gray.shape[:2]
result = np.zeros([h, w*3], dtype=gray.dtype)
result[0:h,0:w] = gray
result[0:h,w:2*w] = t#result1
result[0:h,2*w:3*w] = edges
result = cv.resize(result, (w*3,h ))

# 记录出图
''''
now = datetime.now()
a = now.strftime('%d%H%M')
a ='E:\\'  + a + '.jpg '
cv.imwrite(a, result)
'''
cv.imshow("result", result)


#  阈值测试
ret, th1 = cv.threshold(binary, 127, 255, cv.THRESH_BINARY)
ret, th2 = cv.threshold(binary, 127, 255, cv.THRESH_BINARY_INV)
ret, th3 = cv.threshold(binary, 127, 255, cv.THRESH_TRUNC)
ret, th4 = cv.threshold(binary, 127, 255, cv.THRESH_TOZERO)
ret, th5 = cv.threshold(binary, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]
# 使用Matplotlib显示
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
plt.show()


k = cv.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()