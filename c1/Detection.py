import cv2 as cv
import numpy as np

img = cv.imread("E:\k1.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)

#预处理
def contours_info(_):
    gray = cv.cvtColor(_, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    canny = cv.Canny((binary),10,100)
    #cv.imshow(str(_),canny)
    #contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return canny,gray
binary,gray = contours_info(img)
#在二值图像中查找直线 霍夫曼直线
'''
lines = cv.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 1000) #HoughLines(image, rho像素, theta弧度, threshold累加平面的阈值参数, lines=None, minLineLength=None, maxLineGap=None一条线段的最大允许间隔)
if lines is not None:
    for i in range(len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(img, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)
'''
#查找直线段。
'''
linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 55, None, 50, 10) # same to houghlines
cv.HoughLinesP
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(img, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 5, cv.LINE_AA)
'''
#霍夫曼圆
'''
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 10, None, 101, 100, 20,150 )#cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
for c in circles[0,:]:
    print(c)
    cx, cy, r = c
    cv.circle(img, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
    cv.circle(img, (cx, cy), r, (0, 0, 255), 2, 8, 0)
'''
cv.imshow("Imagea",img)

k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()