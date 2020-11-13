import cv2

# 全局阈值
img_gray = cv2.imread(r"C:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\gray3.tif")
# 自定义阈值
threshold_v = 127

ret,thresh1 = cv2.threshold(img_gray,threshold_v,255,cv2.THRESH_BINARY)

cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_1_"+ str(threshold_v) +".tif", thresh1)