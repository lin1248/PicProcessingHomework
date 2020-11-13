import cv2

# 自适应阈值
img_gray = cv2.imread(r"C:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\gray3.tif")
img_gray= cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)


cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2.tif", thresh1)