import cv2 as cv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
'''
img = cv.imread("E:\p2.jpg",cv.IMREAD_COLOR)
cv.namedWindow("Imagea",cv.WINDOW_NORMAL)
cv.imshow("Imagea",img)
now = datetime.now()
print(now.strftime('%d%H%M'))
a = now.strftime('%d%H%M')
a ='E:\\'  + a + '.jpg '
print(a)
cv.imwrite(a, img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
#预处理
def contours_info(_):
    gray = cv.cvtColor(_, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 9)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    canny = cv.Canny((binary),10,100)
    #cv.imshow(str(_),canny)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours
#  阈值测试
def thre(binary,img):
    ret, th1 = cv.threshold(binary, 127, 255, cv.THRESH_BINARY)
    ret, th2 = cv.threshold(binary, 127, 255, cv.THRESH_BINARY_INV)
    ret, th3 = cv.threshold(binary, 127, 255, cv.THRESH_TRUNC)
    ret, th4 = cv.threshold(binary, 127, 255, cv.THRESH_TOZERO)
    ret, th5 = cv.threshold(binary, 127, 255, cv.THRESH_TOZERO_INV)
    titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, th1, th2, th3, th4, th5]
    # 使用Matplotlib显示
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i], fontsize=8)
        plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
    plt.show()
# 记录出图
def outdraw(result):
    now = datetime.now()
    a = now.strftime('%d%H%M')
    a ='E:\\'  + a + '.jpg '
    cv.imwrite(a, result)
# 成图
def result_out(_1,_2,_3):
    h, w = _1.shape[:2]
    result = np.zeros([h, w*3], dtype=_1.dtype)
    result[0:h,0:w] = _1
    result[0:h,w:2*w] = _2
    result[0:h,2*w:3*w] = _3
    result = cv.resize(result, (w*3,h ))
    return result


k = cv.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv.destroyAllWindows()
