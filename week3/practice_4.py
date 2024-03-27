import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Load the image
img = cv.imread('img/george.jpg', 0)

# Plot the original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img)

cropped_img = img[100:300, 100:300]

# Plot the cropped image
plt.subplot(1, 2, 2)
plt.title('Cropped Image')
plt.imshow(cropped_img)

cv.imwrite('img/cropped_george.jpg', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
