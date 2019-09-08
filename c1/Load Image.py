import cv2
import numpy as np
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread("E:\DSC00006.jpg",cv2.IMREAD_COLOR)#彩照               # 读入黑白图片   ,cv2.IMREAD_GRAYSCALE)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb )     # rgb to >>>> cv.COLOR_BGR2HSV  cv.COLOR_BGR2YUV   cv.COLOR_BGR2YCrCb  cv2.COLOR_BGR2GRAY   转化后所代表的内容不同

#创建窗口并显示图像
cv2.namedWindow("Imagea",cv2.WINDOW_NORMAL)  #cv2.WINDOW_NORMAL   WINDOW_AUTOSIZE
cv2.imshow("Imagea",gray)
gray = np.float32(img)
print(gray)
k = cv2.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv2.destroyAllWindows()

