import cv2 as cv
import numpy as np


#cv.namedWindow("input", cv.WINDOW_NORMAL)
m4 = np.zeros([10,10], np.uint8)
cv.imshow("m3", m4)
gray = np.float32(m4)
print(gray)
m4[2:8,2:8] = 50
gray = np.float32(m4)
print(gray)
cv.imshow("m4",gray)
m5 = np.zeros([100,100,1],np.uint8)
print(m5)
m5 = np.float32(m5)
cv.imshow('m6',m5)
cv.waitKey(0)
cv.destroyAllWindows()