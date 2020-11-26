# 测试mergedRect功能
from mergedRect import mergedRect
import numpy as np
import cv2


filename = "roi2"
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
    if( x.size < 50000 and x.size > 100):
    # if (x.size == 184):
    # if True:
        newContours.append(x)
        count = count + 1
        # print(x.shape)
        # print(x.size)
print("count :" + str(count))

lastContours = []
# 合并长方形
for c in newContours:
    x,y,w,h = cv2.boundingRect(c)
    if w*h < 1000000 and w*h > 1000:
        lastContours.append([x,y,x+w,y+h])

print("len:"+str(len(lastContours)))

for i in range(len(lastContours)-1):
    j = i + 1
    while(j <= len(lastContours)-1):
        minx1,miny1,maxx1,maxy1 = lastContours[i]
        print(minx1,miny1,maxx1,maxy1)
        minx2,miny2,maxx2,maxy2 = lastContours[j]
        print("j::::" + str(j))
        print(minx2,miny2,maxx2,maxy2)
        print("///")
        a,b,c,d = mergedRect(minx1,miny1,maxx1,maxy1,minx2,miny2,maxx2,maxy2)
        if a != -1:
            print("-1")
            print(a,b,c,d)
            print(str(j)+"::"+str(lastContours[j]))
            # print(str(j+1)+"::"+str(lastContours[j+1]))
            lastContours[i]= [a,b,c,d]
            print("删除的为"+str(lastContours.pop(j)))
            # print(str(j)+"::"+str(lastContours[j]))
            # print(str(j+1)+"::"+str(lastContours[j+1]))
            print("len"+str(len(lastContours)))
            j = i + 1
        else:
            j=j+1
print(len(lastContours))



for x in lastContours:
    a,b,c,d = x
    if(c-a)*(d-b) > 1000 and (c-a)/(d-b)<10 and (c-a)/(d-b)>0.1 :
        cv2.rectangle(origin_img,(a,b),(c,d),(0,255,0),2)

cv2.imwrite(filename+"_result.png",origin_img)

