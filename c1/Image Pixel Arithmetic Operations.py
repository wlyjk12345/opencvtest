import cv2
import numpy as  ny
img = cv2.imread("E:\k3.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("E:\k1.jpg",cv2.IMREAD_COLOR)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
#c = ny.zeros(img.shape,img.dtype)
#cv2.divide (img,img2,c)            #subtract    multiply    divide   add
c =cv2.applyColorMap(img,cv2.COLORMAP_COOL)        #COLORMAP_COOL   COLORMAP_JET
c = cv2.resize(c, (200,200) ,interpolation=cv2.INTER_CUBIC)
cv2.imshow("img",c)


h,w,ch = img.shape
print(h,w,ch)
k = cv2.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv2.destroyAllWindows()