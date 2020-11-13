import cv2

# 全局阈值
img_gray = cv2.imread(r"C:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\gray_median.tif")
# 自定义阈值
threshold_v = 127

ret,thresh1 = cv2.threshold(img_gray,threshold_v,255,cv2.THRESH_BINARY)

cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\bin_1_median_"+ str(threshold_v) +".tif", thresh1)