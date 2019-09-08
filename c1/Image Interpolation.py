import cv2 as cv

src = cv.imread("E:\p2.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("m4",src)
h, w, ch = src.shape
print(h, w)

dst = cv.resize(src, (w*2, h*2), fx=0.75, fy=0.75, interpolation=cv.INTER_NEAREST)
cv.imshow("INTER_NEAREST", dst)

dst = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_LINEAR)
cv.imshow("INTER_LINEAR", dst)

dst = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_CUBIC)
cv.imshow("INTER_CUBIC", dst)

dst = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_LANCZOS4)
cv.imshow("INTER_LANCZOS4", dst)

# cv.warpAffine()

cv.waitKey(0)
cv.destroyAllWindows()