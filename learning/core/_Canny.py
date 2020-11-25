import cv2

img = cv2.imread("image/roi3.tif",0)

r1 = cv2.Canny(img, 200, 255)
cv2.imwrite("processed/3/canny.tif", r1)


# cv2.imshow("img",img)
# cv2.waitKey(0)