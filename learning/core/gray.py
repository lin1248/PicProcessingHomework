import cv2

# 1、灰度化处理
# 读入文件
img = cv2.imread(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\image\roi3.tif")
# 灰度化处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# 均值滤波
gray_mean = cv2.blur(gray,(5,5))
# 中值滤波
gray_median = cv2.medianBlur(gray, 5)
# 高斯滤波
gray_Guassian = cv2.GaussianBlur(gray,(5,5),0)


cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\gray3.tif", gray)
cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\gray3_mean.tif", gray_mean)
cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\gray3_Guassian.tif", gray_Guassian)