import cv2 as cv
import numpy as np
img = cv.imread("E:\k2.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)
cv.imshow("Imagea",img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
canny = cv.Canny((binary),10,100)
cv.imshow('dd',canny)
# 轮廓发现
contours, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)#二值图
#    cv2.RETR_EXTERNAL表示只检测外轮廓cv2.RETR_LIST检测的轮廓不建立等级关系 cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
#    cv2.RETR_TREE建立一个等级树结构的轮廓。  返回一个是轮廓本身，还有一个是每条轮廓对应的属性
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    # x, y, w, h = cv.boundingRect(contours[c]);
    # cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)
    # cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0);
    area = cv.contourArea(contours[c]) # 计算面积
    '''
    arclen = cv.arcLength(contours[c], True) #计算弧长， True表示闭合区域
    if area < 100 or arclen < 100:
        continue
    '''
    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(img,[box],0,(0,0,255),2)
    cv.circle(img, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    cv.imshow('dd',img)
cv.drawContours(gray,contours,-1,(0,0,255),3)
#cv2.drawContours(image, contours, contourIdx#哪条轮廓 -1 all , color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]]
# 显示
cv.imshow('contours-demo', gray)




k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()

