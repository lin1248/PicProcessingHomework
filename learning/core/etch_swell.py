import cv2
import numpy as np

img = cv2.imread(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2.tif")

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))         #定义矩形结构元素

# closed1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=1)    #闭运算1
# closed2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=3)    #闭运算2
# opened1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=1)     #开运算1
# opened2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=3)     #开运算2
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)             #梯度

# #显示如下腐蚀后的图像
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_closed1.tif", closed1)
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_closed2.tif", closed2)
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_open1.tif", opened1)
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_open2.tif", opened2)
# cv2.imwrite(r"c:\Users\Mumu\Desktop\PicProcessing\learning\core\processed\3\bin_2_gradient.tif", gradient)
