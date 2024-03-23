import cv2

image = cv2.imread("img/anderson.jpg")

# The split method separates color spaces
B, G, R = cv2.split(image)

# Corresponding channels are separated
cv2.imshow("Original", image)
cv2.waitKey(0)

cv2.imshow("Blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("Red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
