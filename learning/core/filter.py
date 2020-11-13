import cv2

img = cv2.imread(r"C:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2.tif")

# 低通滤波(均值模糊)，模糊,
# （1, 15）是垂直方向模糊，（15， 1）是水平方向模糊
# img_LP = cv2.blur(img, (1, 15))    
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_LP.tif", img_LP)

# 高通滤波，突出细节
# x=cv2.Sobel(img,cv2.CV_16S,1,0)
# y=cv2.Sobel(img,cv2.CV_16S,0,1)

# absx=cv2.convertScaleAbs(x)
# absy=cv2.convertScaleAbs(y)
# dist=cv2.addWeighted(absx,0.5,absy,0.5,0)

# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_HP.tif", dist)

# 高斯滤波
# img_Guassian = cv2.GaussianBlur(img_LP,(5,5),0)
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_LP_Guassian.tif", img_Guassian)

# 中值滤波
img_median = cv2.medianBlur(img,3)
cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_median.tif", img_median)

# 高通滤波，突出细节
# x=cv2.Sobel(img_median,cv2.CV_16S,1,0)
# y=cv2.Sobel(img_median,cv2.CV_16S,0,1)

# absx=cv2.convertScaleAbs(x)
# absy=cv2.convertScaleAbs(y)
# dist=cv2.addWeighted(absx,0.5,absy,0.5,0)

# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_median_HP.tif", dist)