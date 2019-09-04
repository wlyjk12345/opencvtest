import cv2 as cv
import numpy as np

src = cv.imread("E:\DSC00006.jpg")
cv.namedWindow("input", cv.WINDOW_NORMAL)
cv.imshow("input", src)
m3 = cv.resize(src , (200,200) ,interpolation=cv.INTER_CUBIC)    #change size     cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) → dst

h, w, ch = m3.shape
print("h , w, ch", h, w, ch)
for row in range(h):
    for col in range(w):
        b, g, r = m3[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        m3[row, col] = [b, g, r]
cv.imshow("output", m3)

cv.waitKey(0)
cv.destroyAllWindows()