import cv2 as cv
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



k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()
