import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Load the image
image = cv.imread('img/george.jpg', 0)
rows, cols = image.shape

# Plot the original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)

M = np.float32([[1, 0, 100], [0, 1, 50]])
trans1 = cv.warpAffine(image, M, (cols, rows))

# Plot the translated image
plt.subplot(1, 2, 2)
plt.title('Translated Image')
plt.imshow(trans1)

cv.waitKey(0)
cv.destroyAllWindows()
