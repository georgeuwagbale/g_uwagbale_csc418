import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/george.jpg', 0)
rows, cols = img.shape

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img)

M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

plt.subplot(1, 2, 2)
plt.title('Sheared Image Y-axis')
plt.imshow(sheared_img)

cv.imshow('Sheared Image Y-axis', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()
