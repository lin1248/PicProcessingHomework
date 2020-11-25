import cv2
import numpy as np

img=cv2.imread("processed/3/canny.tif",0)
kernel = np.ones((3,3),np.uint8)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT ,kernel)
cv2.imshow('blackhat ',blackhat )
cv2.waitKey(0)