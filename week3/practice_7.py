import cv2 as cv

# Load the image
img = cv.imread('img/george.jpg', 0)

cv.imshow('Original Image', img)
cv.waitKey(0)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gaussian)
cv.waitKey(0)

# Median Blur
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)
cv.waitKey(0)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Blur', bilateral)
cv.waitKey(0)
cv.destroyAllWindows()
