import cv2

# 1、灰度化处理
# 读入文件
img = cv2.imread("image/roi1.tif")

# 灰度化处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# 均值滤波
gray_mean = cv2.blur(gray,(5,5))
# 中值滤波
gray_median = cv2.medianBlur(gray, 5)
# 高斯滤波
gray_Guassian = cv2.GaussianBlur(gray,(5,5),0)


cv2.imwrite("processed/1/gray1.tif", gray)
cv2.imwrite("processed/1/gray1_mean.tif", gray_mean)
cv2.imwrite("processed/1/gray1_Guassian.tif", gray_Guassian)