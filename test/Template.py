import cv2 as cv
import numpy as np
img = cv.imread("E:\p4.jpg",cv.IMREAD_COLOR)
cv.namedWindow("result",cv.WINDOW_NORMAL)
img = cv.edgePreservingFilter(img, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)  #保边滤波器
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray= cv.medianBlur(gray, 9)
result1 = cv.GaussianBlur(gray, (9, 9), 0)
#dst = cv.pyrMeanShiftFiltering(img, 15, 30, termcrit=(cv.TERM_CRITERIA_MAX_ITER+cv.TERM_CRITERIA_EPS, 5, 1))

'''# 顶帽操作
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_TOPHAT, se)
edges = cv.Canny((result1),1,10)
'''
dst = cv.Laplacian(result1, cv.CV_32F, ksize=3, delta=127) #
dst = cv.convertScaleAbs(dst)

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpen_image = cv.filter2D(dst, cv.CV_32F, sharpen_op)
sharpen_image = cv.convertScaleAbs(sharpen_image)

edges = cv.Canny((dst),1,10)
h, w = gray.shape[:2]
result = np.zeros([h, w*3], dtype=gray.dtype)
result[0:h,0:w] = result1
result[0:h,w:2*w] = dst
result[0:h,2*w:3*w] =
result = cv.resize(result, (w*2,h ))

cv.imshow("result", result)


k = cv.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()