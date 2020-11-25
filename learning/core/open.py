import cv2
import numpy as np

img = cv2.imread("processed/3/canny.tif",0)

kernel = np.ones((1,1),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)
cv2.waitKey(0) 