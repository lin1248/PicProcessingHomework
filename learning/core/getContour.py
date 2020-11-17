import cv2

num = 1

# 获取图像
origin_img = cv2.imread("image/roi" + str(num) + ".tif")
print(1)
# gray_img = cv2.cvtColor(origin_img,cv2.COLOR_BGR2GRAY)
bin_img = cv2.imread("processed/"+ str(num) +"/bin_2.tif")
print(2)
bin_img = cv2.cvtColor(bin_img,cv2.COLOR_BGR2GRAY)
print(3)
contours,hierarchy = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(4)
result_img = cv2.drawContours(origin_img,contours,-1,(0,0,255),3)
print(5)
cv2.imwrite("processed/result/bin_2_result"+ str(num) +".tif",result_img)



