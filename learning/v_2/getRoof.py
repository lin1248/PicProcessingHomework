# 测试mergedRect功能
from mergedRect import mergedRect
import numpy as np
import cv2
from function import * 



filename = "roi2"
# 获取图像
origin_img = cv2.imread("../core/image/"+filename+".tif")



# 预处理，将图片缩放
origin_img = cv2.pyrDown(origin_img)


# 形态学：边缘检测
img_gray = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("img/img_gray.png",img_gray)

img_gray = cv2.GaussianBlur(img_gray,(3,3),0)

cv2.imwrite("img/img_gray_Gaussian.png",img_gray)

_,Thr_img = cv2.threshold(img_gray,180,255,cv2.THRESH_BINARY)

cv2.imwrite("img/bin_img.png",Thr_img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))         #定义矩形结构元素
bin_img = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度

cv2.imwrite("img/bin_mor.png",bin_img)

bin_img = cv2.Canny(bin_img, 100, 200)

cv2.imwrite("img/canny.png",bin_img)

# 方框滤波
bin_img = cv2.boxFilter(bin_img, -1, (3, 3), normalize = 0)

cv2.imwrite("img/final_bin_img.png",bin_img)


# 提取轮廓
contours,hierarchy = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(type(contours))
print(len(contours))
count = 0
newContours = []
for x in contours:
    if( x.size < 10000 and x.size > 200):
    # if True:

        newContours.append(x)
        count = count + 1
print("count :" + str(count))

lastContours = []
# 去掉过大或者过小的轮廓
for c in newContours:
    x,y,w,h = cv2.boundingRect(c)
    if w*h < 50000 and w*h > 5000:

        lastContours.append([x,y,x+w,y+h])

print("len:"+str(len(lastContours)))

i = 0
while(i < len(lastContours)-1):
    # j = i + 1
    j = 1 if i == 0 else 0
    while(j <= len(lastContours)-1):
        print("现在i,j为" +str(i)+"," +str(j) )
        minx1,miny1,maxx1,maxy1 = lastContours[i]
        print(minx1,miny1,maxx1,maxy1)
        minx2,miny2,maxx2,maxy2 = lastContours[j]
        print("j::::" + str(j))
        print(minx2,miny2,maxx2,maxy2)
        print("///")
        a,b,c,d = mergedRect(minx1,miny1,maxx1,maxy1,minx2,miny2,maxx2,maxy2)
        # 判断两个矩形是否可以合并
        if a != -1:
            print("发现可以合并，现在i,j为" +str(i)+"," +str(j) )
            print(a,b,c,d)
            print(str(j)+"::"+str(lastContours[j]))
            if(j>i):
                lastContours[i]= [a,b,c,d]
                print("删除的为"+str(lastContours.pop(j)))
            else:
                lastContours[j]= [a,b,c,d]
                print("删除的为"+str(lastContours.pop(i)))
                i = j

            print("len"+str(len(lastContours)))
            # 合并之后需要从头开始遍历
            j = 1 if i == 0 else 0
        else:
            print("现在i,j为" +str(i)+"," +str(j) )
            if(i == j+1):
                j = i + 1
            else:
                j = j + 1
    i = i + 1
print(len(lastContours))



for x in lastContours:
    a,b,c,d = x
    cv2.drawContours(origin_img,newContours,-1,(0,0,255),3)

cv2.imwrite("img/"+filename+"_contours.png",origin_img)

for x in lastContours:
    a,b,c,d = x
    cv2.rectangle(origin_img,(a,b),(c,d),(0,255,0),2)
    cv2.circle(origin_img,((c+a)//2,(d+b)//2),5,(255,0,0), 8)


cv2.imwrite("img/"+filename+"_result.png",origin_img)

