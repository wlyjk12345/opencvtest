import cv2 as cv
import numpy as np
cv.namedWindow("image",cv.WINDOW_NORMAL)
k3 = cv.imread("E:\k3.jpg",cv.IMREAD_COLOR)
k3 = cv.flip(k3,-1)    # 0 x 1 y -1 xy
'''
m4 = np.zeros([100,100], np.uint8)
m4[20:40,20:40] = 255


 # custom
h, w,l = k3.shape
print(h, w)
for x in range(h):  
    for y in range(w):
        b,g,r =k3[x,y]
        k3[h-x-1,y] = b,g,r
'''
cv.imshow('image',k3)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()