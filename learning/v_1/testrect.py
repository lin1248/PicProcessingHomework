# 测试mergedRect功能
from mergedRect import mergedRect
import numpy as np
import cv2



filename = "roi3"
# 获取图像
origin_img = cv2.imread("../core/image/"+filename+".tif")

# 预处理，将图片缩放
# origin_img = cv2.pyrDown(origin_img)

# canny(): 边缘检测
# img1 = cv2.GaussianBlur(origin_img,(3,3),0)
# bin_img = cv2.Canny(img1, 100, 200)

# cv2.imshow("origin_img",bin_img)
# cv2.waitKey(0)

# 形态学：边缘检测
img_gray= cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
_,Thr_img = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
# _,Thr_img_1 = cv2.threshold(img_gray,110,255,cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))         #定义矩形结构元素
bin_img = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度

# bin_img = cv2.GaussianBlur(bin_img,(3,3),0)
# bin_img = cv2.Canny(bin_img, 100, 200)

# 方框滤波
# bin_img = cv2.boxFilter(bin_img, -1, (3, 3), normalize = 0)

cv2.imwrite("bin_img.png",bin_img)

# 滤波


# # 灰度
# img_gray= cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
# # 自适应阈值二值化
# bin_img = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
# # 手动阈值
# # ret,bin_img = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)

# 创建矩形结构单元
# g=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# 帽处理
# bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_TOPHAT, g)
# cv2.imwrite("Blcakhat_img.png",bin_img)

# origin_img,bin_img = getProcessedBin(filename)

# 提取轮廓
contours,hierarchy = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(type(contours))
print(len(contours))
count = 0
newContours = []
for x in contours:
    # if( x.size < 30000 and x.size > 200):
    # if (x.size == 184):
    if True:
        newContours.append(x)
        count = count + 1
        # print(x.shape)
        # print(x.size)
print("count :" + str(count))

lastContours = []
# 去掉过大或者过小的轮廓
for c in newContours:
    x,y,w,h = cv2.boundingRect(c)
    # if w*h < 50000 and w*h > 1000:
    if True:
        lastContours.append([x,y,x+w,y+h])

print("len:"+str(len(lastContours)))

# i = 0
# while(i < len(lastContours)-1):
#     # j = i + 1
#     j = 1 if i == 0 else 0
#     while(j <= len(lastContours)-1):
#         print("现在i,j为" +str(i)+"," +str(j) )
#         minx1,miny1,maxx1,maxy1 = lastContours[i]
#         print(minx1,miny1,maxx1,maxy1)
#         minx2,miny2,maxx2,maxy2 = lastContours[j]
#         print("j::::" + str(j))
#         print(minx2,miny2,maxx2,maxy2)
#         print("///")
#         a,b,c,d = mergedRect(minx1,miny1,maxx1,maxy1,minx2,miny2,maxx2,maxy2)
#         # 判断两个矩形是否可以合并
#         if a != -1:
#             print("发现可以合并，现在i,j为" +str(i)+"," +str(j) )
#             print(a,b,c,d)
#             print(str(j)+"::"+str(lastContours[j]))
#             if(j>i):
#                 lastContours[i]= [a,b,c,d]
#                 print("删除的为"+str(lastContours.pop(j)))
#             else:
#                 lastContours[j]= [a,b,c,d]
#                 print("删除的为"+str(lastContours.pop(i)))
#                 i = j

#             print("len"+str(len(lastContours)))
#             # 合并之后需要从头开始遍历
#             # j = i + 1
#             j = 1 if i == 0 else 0
#         else:
#             print("现在i,j为" +str(i)+"," +str(j) )
#             if(i == j+1):
#                 j = i + 1
#             else:
#                 j = j + 1
#     i = i + 1
# print(len(lastContours))



for x in lastContours:
    a,b,c,d = x
    if(c-a)*(d-b) > 2000 and (c-a)/(d-b)<10 and (c-a)/(d-b)>0.1 and (c-a)*(d-b) < 70000:
    # if True:
        cv2.rectangle(origin_img,(a,b),(c,d),(0,255,0),2)
        cv2.circle(origin_img,((c+a)//2,(d+b)//2),5,(255,0,0), 8)

cv2.imwrite(filename+"_result.png",origin_img)

