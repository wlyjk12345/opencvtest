import cv2
img = cv2.imread("E:\DSC00006.jpg",cv2.IMREAD_COLOR)
cv2.namedWindow("Imagea",cv2.WINDOW_NORMAL)
cv2.imshow("Imagea",gray)





k = cv2.waitKey(0)
#释放窗口
if k==27:
   # 如果输入ESC退出
   cv2.destroyAllWindows()
