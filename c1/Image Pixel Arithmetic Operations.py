import cv2
import numpy as  ny
img = cv2.imread("E:\k3.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("E:\k1.jpg",cv2.IMREAD_COLOR)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
#c = ny.zeros(img.shape,img.dtype)

#cv2.divide (img,img2,c)            #subtract    multiply    divide   add         线性代数 矩阵

dst1 = cv2.bitwise_not(img)    # _and 每个像素值进行二进制“与”  _or 或  _xor 异或 _not非
img3 = cv2.resize(img, (1080,1660) ,interpolation=cv2.INTER_CUBIC)
dst2 = cv2.bitwise_not(img2,img3)

#c =cv2.applyColorMap(img,cv2.COLORMAP_COOL)        #COLORMAP_COOL   COLORMAP_JET


cv2.imshow("img",dst2)

h,w,ch = img2.shape
print(h,w,ch)
k = cv2.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv2.destroyAllWindows()