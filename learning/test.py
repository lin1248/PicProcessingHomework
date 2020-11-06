import cv2

# img = cv2.imread(r"C:\Users\Mumu\Desktop\PicProcessing\learning\test.jpg")
# h = 50
# x_center = 264
# y_center = 200
 
# draw_0 = cv2.rectangle(img, (x_center-h, y_center-h), (x_center+h, y_center+h), (255, 100, 250), 2)
# cv2.imshow('German',draw_0)
# cv2.waitKey()

from test2 import detect_face
img = cv2.imread(r"C:\Users\Mumu\Desktop\PicProcessing\learning\face.jpg")
detect_face(img)