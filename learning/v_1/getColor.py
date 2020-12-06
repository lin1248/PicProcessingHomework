import cv2
import numpy as np
from function import *

# def getProcessedBin(filename):
filename = "roi2"
# 获取图像
origin_img = cv2.imread("../core/image/"+filename+".tif")

# range of green
lower_green = np.array([36,25,25])
upper_green = np.array([70,255,255])
# set blue thresh
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])
# range of red
lower_red = np.array([0,43,46])
upper_red = np.array([10,255,255])
# range of roof
lower_roof = np.array([0,0,46])
upper_roof = np.array([180,43,220])



img_gray = cv2.cvtColor(origin_img,cv2.COLOR_BGR2GRAY)
# bin_img = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
_,Thr_img = cv2.threshold(img_gray,1127,255,cv2.THRESH_BINARY)

hsv = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
mask_g = cv2.inRange(hsv, lower_green, upper_green)

mask_b = cv2.inRange(hsv,lower_blue, upper_blue)
mask_r = cv2.inRange(hsv,lower_red,upper_red)
mask_gray = cv2.inRange(hsv,lower_roof,upper_roof)


bin_img = Thr_img+mask_b-mask_g+mask_r-mask_gray

cv2.imwrite("bin.png",bin_img)
cv2.imwrite("green.png",mask_g)
# cv2.imwrite("yellow.png",mask_y)
cv2.imwrite("blue.png",mask_b)
cv2.imwrite("red.png",mask_r)
cv2.imwrite("gray.png",mask_gray)
# cv2.imwrite("black.png",mask_black)

# 滤波
bin_img = medianFilter(bin_img)
cv2.imwrite("medianFilter.png",bin_img)

# 闭运算
bin_img = close(mask_gray)
cv2.imwrite("close.png",bin_img)
# 开运算
bin_img = open(mask_gray)
cv2.imwrite("open.png",bin_img)

bin_img = cv2.Canny(bin_img, 200, 255)
cv2.imwrite("canny.png",bin_img)


contours,hierarchy = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    x,y,w,h=cv2.boundingRect(contours[c])
    # if(w*h > 10000 and w*h < 10000000):
    if True:
        cv2.rectangle(origin_img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.circle(origin_img,((2*x+w)//2,(2*y+h)//2),5,(255,0,0), 8)
        # cv2.drawContours(origin_img, contours,c, (0, 0, 255), 2, 8)

cv2.imwrite("origin_img.png",origin_img)


    # return origin_img,bin_img
