import cv2 as cv
import numpy as np

src = np.zeros([10,10],np.uint8)
src[2:4,2:4] = 60
#src = cv.imread("E:\p2.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)
cv.imshow("binary",src)




min, max, minLoc, maxLoc = cv.minMaxLoc(src)      # void minMaxLoc( const Mat& src,  double* minVal, double* maxVal=0, Point* minLoc=0, Point* maxLoc=0, const Mat& mask=Mat() );
print("min: %.2f, max: %.2f"% (min, max))
print("min loc: ", minLoc)
print("max loc: ", maxLoc)

means, stddev = cv.meanStdDev(src)    #src：输入矩阵，这个矩阵应该是1-4通道的，这可以将计算结果存在Scalar_mean：输出参数，计算均值，stddev：输出参数，计算标准差
print("mean: %.2f, stddev: %.2f"% (means, stddev))
src[np.where(src < means)] = 0
src[np.where(src > means)] = 255
cv.imshow("binary", src)


cv.waitKey(0)
cv.destroyAllWindows()