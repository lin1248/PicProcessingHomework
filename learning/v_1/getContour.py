import cv2
import numpy as np
from mergedRect import mergedRect

# g=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

filename = "roi3"
# 获取图像
origin_img = cv2.imread("../core/image/"+filename+".tif")
# 灰度
img_gray= cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
# 自适应阈值二值化
bin_img = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)


contours,hierarchy = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(type(contours))
print(len(contours))
count = 0
newContours = []
for x in contours:
    # if( x.size < 50000 and x.size > 100):
    if (x.size == 108):
    # if True:
        newContours.append(x)
        count = count + 1
        # print(x.shape)
        # print(x.size)
print("count :" + str(count))

# 在白底上画出轮廓
temp = np.ones(bin_img.shape,np.uint8)*255
temp = cv2.drawContours(temp, contours, -1, (0, 0, 255), 3)
cv2.imwrite(filename+"contours.png",temp)


ncount = count
for c in range(len(newContours)):
    # print(type(newContours[c]))
    x,y,w,h=cv2.boundingRect(newContours[c])
    # print("x,y,w,h=" +str(x) + "//" +str(y) + "//"+str(w)+"//"+str(h))
    if(w*h > 1000):
    # if True:
        ncount = ncount - 1
        cv2.rectangle(origin_img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.drawContours(origin_img, newContours, c, (0, 0, 255), 2, 8)
print(count - ncount)

cv2.imwrite(filename+"_result.png",origin_img)



