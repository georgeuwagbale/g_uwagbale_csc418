import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/george.jpg', 0)

# Plot the original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img)

rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, -1, rows], [0, 0, 1]])
reflected_img = cv.warpPerspective(img, M, int(cols), int(rows))

# Plot the reflected image
plt.subplot(1, 2, 2)
plt.title('Reflected Image')
plt.imshow(reflected_img)

cv.imwrite('img/reflected_george.jpg', reflected_img)
cv.waitKey(0)
cv.destroyAllWindows()
