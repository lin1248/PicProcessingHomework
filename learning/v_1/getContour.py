import cv2

g=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

# 获取图像
origin_img = cv2.imread("roi3.tif")
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
        newContours.append(x)
        count = count + 1
        print(x.shape)
        print(x.size)
print("count :" + str(count))

# result_img = cv2.drawContours(origin_img,newContours,-1,(0,0,255),3)
ncount = count
for c in range(len(newContours)):
    # rect = cv2.minAreaRect(newContours[c])
    # cx, cy = rect[0]
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)
    # cv2.drawContours(img,[box],0,(0,255,0),2)
    # cv2.circle(img, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    x,y,w,h=cv2.boundingRect(newContours[c])
    #Straight Bounding Rectangle
    if(w*h > 2000):
        ncount = ncount - 1
        cv2.rectangle(origin_img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.drawContours(origin_img, newContours, c, (0, 0, 255), 2, 8)
print(count - ncount)

cv2.imwrite("result3.png",origin_img)



