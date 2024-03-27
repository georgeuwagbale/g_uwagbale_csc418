import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/george.jpg', 0)

# Plot the original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img)

rows, cols = img.shape
img_rotation = cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), 45, 1), (cols, rows))

# Plot the rotated image
plt.subplot(1, 2, 2)
plt.title('Rotated Image')
plt.imshow(img_rotation)

cv.imshow('Rotated Image', img_rotation)
cv.imwrite('img/rotated_george.jpg', img_rotation)
cv.waitKey(0)
cv.destroyAllWindows()
