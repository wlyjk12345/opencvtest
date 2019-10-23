import cv2 as cv
import numpy as np
img = cv.imread("E:\k2.jpg",cv.IMREAD_COLOR)
src = img
src2 = cv.imread("E:\k1.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)
cv.imshow("Imagea",img)
#预处理
def contours_info(_):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    canny = cv.Canny((binary),10,100)
    #    cv.imshow(str(_),canny)
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours
    # 轮廓发现
#contours, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)#二值图
#contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#    cv2.RETR_EXTERNAL表示只检测外轮廓cv2.RETR_LIST检测的轮廓不建立等级关系 cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
#    cv2.RETR_TREE建立一个等级树结构的轮廓。  返回一个是轮廓本身，还有一个是每条轮廓对应的属性
contours = contours_info(img)
contours2 = contours_info(src2)

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
    if area < 10 or arclen < 10:  # 控制大小等
        continue

    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    box = np.int0(box)
    #cv.drawContours(img,[box],0,(0,0,255),2)
    #cv.circle(img, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    cv.imshow('dd',img)

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
# 轮廓匹配
for c in range(len(contours)):
    mm = cv.moments(contours[c])
    mm2 = cv.moments(contours2[c])
    hum2 = cv.HuMoments(mm2)
    hum = cv.HuMoments(mm)
    dist = cv.matchShapes(hum, hum2, cv.CONTOURS_MATCH_I1, 0)
    if dist < 1:
        cv.drawContours(src, contours, c, (255, 0, 255), 2, 8)
    print("dist %f"%(dist))
cv.imshow('d',src)

#cv.drawContours(gray,contours,-1,(0,0,255),3)
#cv2.drawContours(image, contours, contourIdx#哪条轮廓 -1 all , color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]]
# 显示
#cv.imshow('contours-demo', gray)




k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()

