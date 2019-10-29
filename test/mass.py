# 预处理
shape_op = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], np.float32)
img = cv.filter2D(img, -1, shape_op)
#img = cv.edgePreservingFilter(img, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)  #保边滤波器
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#gray= cv.medianBlur(gray, 9)
#result1 = cv.GaussianBlur(gray, (9, 9), 0)
binary =  gray
#dst = cv.pyrMeanShiftFiltering(img, 15, 30, termcrit=(cv.TERM_CRITERIA_MAX_ITER+cv.TERM_CRITERIA_EPS, 5, 1))
#se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))# 顶帽操作
#binary = cv.morphologyEx(result1, cv.MORPH_BLACKHAT, se)
ret, th = cv.threshold(binary, 127, 255, cv.THRESH_BINARY)
#t= cv.GaussianBlur(th, (9, 9), 0)
t = cv.medianBlur(th, 5)
#cv.imshow('d',t)


# 边缘
edges = cv.Canny((t),1,10)
'''
dst = cv.Laplacian(result1, cv.CV_32F, ksize=3, delta=127) #
img = cv.convertScaleAbs(dst)

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpen_image = cv.filter2D(dst, cv.CV_32F, sharpen_op)
sharpen_image = cv.convertScaleAbs(sharpen_image)
'''
#edges = cv.Canny((dst),1,10)