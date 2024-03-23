import cv2

path = "img/Model-82A1-29-BBL-MP.png"

img = cv2.imread(path)

window_name = "Image"

cv2.imshow(window_name, img)

cv2.waitKey(0)

cv2.destroyAllWindows()