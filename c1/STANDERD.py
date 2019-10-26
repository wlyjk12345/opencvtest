import cv2 as cv
import numpy as np
from datetime import datetime
img = cv.imread("E:\p2.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)
cv.imshow("Imagea",img)
now = datetime.now()
print(now.strftime('%d%H%M'))
a = now.strftime('%d%H%M')
a ='E:\\'  + a + '.jpg '
print(a)
cv.imwrite(a, img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#预处理
def contours_info(_):
    gray = cv.cvtColor(_, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    canny = cv.Canny((binary),10,100)
    #cv.imshow(str(_),canny)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours



k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()
