import cv2 as cv
import numpy as np
img = cv.imread("E:\k1.jpg",cv.IMREAD_COLOR)
src = img
src2 = cv.imread("E:\k1.jpg",cv.IMREAD_COLOR)
cv.namedWindow("",cv.WINDOW_NORMAL)
#cv.imshow("Imagea",img)
#预处理
def contours_info(_):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    canny = cv.Canny((binary),10,100)
    #cv.imshow(str(_),canny)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours
    # 轮廓发现
#contours, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)#二值图
#contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#    cv2.RETR_EXTERNAL表示只检测外轮廓cv2.RETR_LIST检测的轮廓不建立等级关系 cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
#    cv2.RETR_TREE建立一个等级树结构的轮廓。  返回一个是轮廓本身，还有一个是每条轮廓对应的属性
contours = contours_info(img)
contours2 = contours_info(src2)
print(len(contours))
# 几何矩计算与hu矩计算
#mm2 = cv.moments(contours2[])
#hum2 = cv.HuMoments(mm2)
# 图像轮廓
'''
for c in range(len(contours)):
    # x, y, w, h = cv.boundingRect(contours[c]);
    # cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)
    # cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0);
    area = cv.contourArea(contours[c]) # 计算面积

    arclen = cv.arcLength(contours[c], True) #计算弧长， True表示闭合区域
    #if area < 10 or arclen < 10:  # 控制大小等
    #    continue

    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(img,[box],0,(0,0,255),2)
    cv.circle(img, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    #cv.imshow('dd',img)
    #cv.imwrite('E:\CannyCounter.jpg',img)
    ww, hh = rect[1]
    ratio = np.minimum(ww, hh) / np.maximum(ww, hh)   # 矩形比率
    print(ratio)
    mm = cv.moments(contours[c])  #图像的几何矩计算
    hum2 = cv.HuMoments(mm)  #hu矩计算
    m00 = mm['m00']
    m10 = mm['m10']
    m01 = mm['m01']
    cx = np.int(m10 / m00)
    cy = np.int(m01 / m00)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    if ratio > 0.9:
        cv.drawContours(src, [box], 0, (0, 0, 255), 2)
        cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    if ratio < 0.5:
        cv.drawContours(src, [box], 0, (255, 0, 255), 2)
        cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (0, 0, 255), 2, 8, 0)
'''
#print(len(contours))
# 轮廓匹配
'''
for c in range(len(contours)):
    mm = cv.moments(contours[c])
    mm2 = cv.moments(contours2[c])
    hum2 = cv.HuMoments(mm2)
    hum = cv.HuMoments(mm)
    dist = cv.matchShapes(hum, hum2, cv.CONTOURS_MATCH_I1, 0)
    if dist < 1:
        cv.drawContours(src, contours, c, (255, 0, 255), 2, 8)
    print("dist %f"%(dist))
'''
# 轮廓多边形逼近
'''   
for c in range(len(contours)):
#最小的多边形
    approx  = cv.approxPolyDP(contours[c],3,True)  #最小的多边形包围
    cv.polylines(src, [approx], True, (0, 0, 255), 2)
cv.imshow("approx",src)
#最外层的"凸"多边形
    ret = cv.isContourConvex(contours[c])  #判定一个轮廓是否是凸包,最外层的"凸"多边形
    points = cv.convexHull(contours[c])  # 寻找凸包，得到凸包的角点
    #cv.polylines(src, [points], True, (0, 255, 0), 2)
    total = len(points)
    print(total)
    for i in range(len(points)):
        x1, y1 = points[i][0]
        x2, y2 = points[(i+1)%total][0]
        cv.circle(src, (x1, y1), 4, (255, 0, 0), 2, 8, 0)
        cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
    print(points)
    print("convex : ", ret)
cv.imshow("contours_analysis", src)
'''
# 椭圆拟合have PROBLEMS#TODO
'''for c in range(len(contours)):    

    (cx, cy), (a, b), angle = cv.fitEllipse(contours[c])
    # 绘制椭圆   #cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])
    cv.ellipse(src, (np.int32(cx), np.int32(cy)),(np.int32(a/2), np.int32(b/2)), angle, 0, 360, (0, 0, 255), 2, 8, 0)
cv.namedWindow("d",cv.WINDOW_NORMAL)
cv.imshow('d',src)
'''
# 直线拟合与极值点寻找
'''
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])#矩形边框（boundingRect），用于计算图像一系列点的外部矩形边界
    m = max(w, h)
    # if m < 30:
    #     continue
    vx, vy, x0, y0 = cv.fitLine(contours[c], cv.DIST_L1, 0, 0.01, 0.01)
    k = vy/vx
    if k == 0:
        continue
    b = y0 - k*x0
    maxx = 0
    maxy = 0
    miny = 100000
    minx = 0
    for pt in contours[c]:
        px, py = pt[0]
        if maxy < py:
            maxy = py
        if miny > py:
            miny = py
    maxx = (maxy - b) / k
    minx = (miny - b) / k
    cv.line(src, (np.int32(maxx), np.int32(maxy)),
            (np.int32(minx), np.int32(miny)), (0, 0, 255), 2, 8, 0)
cv.imshow('',src)
'''
#点到边缘#TODO
'''
image = np.zeros(src.shape, dtype=np.float32)
h, w = src.shape[:2]

for row in range(h):
    for col in range(w):
        dist = cv.pointPolygonTest(contours[0], (col, row), False)  # True的话返回点到轮廓的距离，False则返回+1，0，-1三个值，其中+1表示点在轮廓内部，0表示点在轮廓上，-1表示点在轮廓外
        if dist == 0:
            image[row, col] = (255, 255, 255)
        if dist > 0:
            image[row, col] = (255-dist, 0, 0)
        if dist < 0:
            image[row, col] = (0, 0, 255+dist)

dst = cv.convertScaleAbs(image)  # 将像素点进行绝对值计算
dst = np.uint8(dst)
cv.imshow("contours_analysis", dst)
'''
#cv.drawContours(gray,contours,-1,(0,0,255),3)
#cv2.drawContours(image, contours, contourIdx#哪条轮廓 -1 all , color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]]
# 显示
#cv.imshow('contours-demo', gray)




k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()

