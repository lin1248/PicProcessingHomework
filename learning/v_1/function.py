import cv2
import numpy as np

# 闭运算
def close(bin_img):
    kernel = np.ones((9,9),np.uint8)
    return cv2.morphologyEx(bin_img,cv2.MORPH_CLOSE,kernel)

# 开运算
def open(bin_img):
    kernel = np.ones((9,9),np.uint8)
    return cv2.morphologyEx(bin_img,cv2.MORPH_OPEN,kernel)

def medianFilter(bin_img):
    # 中值滤波
    return cv2.medianBlur(bin_img,3)

def fastFilter(bin_img):
    # 非局部均值去噪
    dst = cv2.fastNlMeansDenoising(bin_img,None,3,7,21)
    cv2.imwrite("fast.png",dst)
    return dst