import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread("img/zion.jpg")

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

# Remove noise using a median filter
filtered_image = cv2.medianBlur(image, 15)

# Save the image
cv2.imwrite('img/median_blur_image.jpg', filtered_image)

# Plot the blured image
plt.subplot(1, 2, 2)
plt.title("Median Blur Image")
plt.imshow(filtered_image)
plt.show()
