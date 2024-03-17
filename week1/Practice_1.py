import cv2

path = "img/lagos.jpg"

img = cv2.imread(path)

window_name = "Image"

cv2.imshow(window_name, img)

cv2.waitKey(0)

cv2.destroyAllWindows()