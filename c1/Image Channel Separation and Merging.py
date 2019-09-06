import cv2
img = cv2.imread("E:\k3.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("E:\k1.jpg",cv2.IMREAD_COLOR)
cv2.namedWindow("output1",cv2.WINDOW_NORMAL)

mv = cv2.split(img)      # 分
mv[2][:, :] = 0         # 0 blue 1 green 2 red
dst1 = cv2.merge(mv)     # 和
cv2.imshow("output1", dst1)




k = cv2.waitKey(0)
if k==27:
   # 如果输入ESC退出
   cv2.destroyAllWindows()