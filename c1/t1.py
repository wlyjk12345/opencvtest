import cv2
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread("E:\DSC00006.jpg",cv2.IMREAD_COLOR)#彩照               # 读入黑白图片   ,cv2.IMREAD_GRAYSCALE)
#创建窗口并显示图像
cv2.namedWindow("Imagea")
cv2.imshow("Imagea",img)
k = cv2.waitKey(0)
#释放窗口
if k==27:  #如果输入ESC退出
   cv2.destroyAllWindows()


