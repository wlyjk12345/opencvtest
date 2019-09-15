import cv2 as cv
import numpy as np
img = cv.imread("E:\p1.png",cv.IMREAD_COLOR)
cv.namedWindow("result",cv.WINDOW_NORMAL)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

result1 = cv.GaussianBlur(gray, (5, 5), 0)

edges = cv.Canny((result1),1,10)

h, w = gray.shape[:2]
result = np.zeros([h, w*2], dtype=gray.dtype)
result[0:h,0:w] = result1
result[0:h,w:2*w] = edges
result = cv.resize(result, (w*2,h ))

cv.imshow("result", result)


k = cv.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()