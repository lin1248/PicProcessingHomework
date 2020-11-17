import cv2

num = 1

# 自适应阈值
img_gray = cv2.imread("processed/" + str(num) + "/gray" + str(num) + ".tif")
img_gray= cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)


cv2.imwrite("processed/" + str(num) + "/bin_2.tif", thresh1)