import cv2 as cv
import numpy as np
cv.namedWindow("image",cv.WINDOW_NORMAL)
p3 = cv.imread("E:\p3.jpg",cv.IMREAD_COLOR)
h, w = p3.shape[:2]
print(h,w)
cv.imshow('image',k3)
dst = cv.resize(p3, (w*2, h*2), fx=0.75, fy=0.75, interpolation=cv.INTER_NEAREST)
cv.imshow("INTER_NEAREST", dst)

dst = cv.resize(p3, (w*2, h*2), interpolation=cv.INTER_LINEAR)
cv.imshow("INTER_LINEAR", dst)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()