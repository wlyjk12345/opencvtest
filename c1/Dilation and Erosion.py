import cv2 as cv
import numpy as np
src = cv.imread("E:\k1.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)

#预处理
def contours_info(_):
    gray = cv.cvtColor(_, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 9)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    #canny = cv.Canny((binary),10,100)
    cv.imshow(str(_),binary)
    #contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return binary
se = np.ones((3, 3), dtype=np.uint8)
#se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))#getStructuringElement(int shape, Size esize, Point anchor = Point(-1, -1))#矩形：MORPH_RECT;交叉形：MORPH_CROSS;椭圆形：MORPH_ELLIPSE;
#dilate = cv.dilate(result1, se, None, (-1, -1), 1)#膨胀与腐蚀
#erode = cv.erode(result1, se, None, (-1, -1), 1)
# 顶帽操作
def Top_Hat(_):
    se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))#void morphologyEx( InputArray src, OutputArray dst, int op, InputArray kernel,Point anchor=Point(-1,-1), int iterations=1,int borderType=BORDER_CONSTANT,const Scalar& borderValue=morphologyDefaultBorderValue() );
    binary = cv.morphologyEx(_, cv.MORPH_BLACKHAT, se)
    return binary
# 黑帽操作
def Black_Hat(_):
    se = cv.getStructuringElement(cv.MORPH_RECT, (9, 9), (-1, -1))
    binary = cv.morphologyEx(_, cv.MORPH_BLACKHAT, se)
    return binary
# 开操作
def open_demo(_):
    se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
    binary = cv.morphologyEx(_, cv.MORPH_OPEN, se)
    return binary
# 闭操作
def close_demo(_):
    se1 = cv.getStructuringElement(cv.MORPH_RECT, (25, 5), (-1, -1))
    se2 = cv.getStructuringElement(cv.MORPH_RECT, (5, 25), (-1, -1))
    binary = cv.morphologyEx(_, cv.MORPH_CLOSE, se1)
    binary = cv.morphologyEx(_, cv.MORPH_CLOSE, se2)
    return binary
# 形态学梯度 - 基本梯度#基本梯度是用膨胀后的图像减去腐蚀后的图像得到差值图像
se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
basic = cv.morphologyEx(src, cv.MORPH_GRADIENT, se)
cv.imshow("basic gradient", basic)

# 外梯度 是用图像膨胀之后再减去原来的图像得到的差值图像
dilate = cv.morphologyEx(src, cv.MORPH_DILATE, se)
exteral = cv.subtract(dilate, src)
cv.imshow("external gradient", exteral)

# 内梯度 是用原图像减去腐蚀之后的图像得到差值图像
erode = cv.morphologyEx(src, cv.MORPH_ERODE, se)
interal = cv.subtract(src, erode)
cv.imshow("interal gradient", interal)


binary = contours_info(src)
se = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, se)
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    area = cv.contourArea(contours[c])
    if area < 200:
        continue
    if h > (3*w) or h < 20:
        continue
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)

#binary = close_demo(result1)
cv.imshow("raw", src)
cv.imshow('result',binary)
k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()