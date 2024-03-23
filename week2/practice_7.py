import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread("img/desmond.jpg")

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

# Inverse by subtracting from 255
inverse_image = 255 - image

# Save the image
cv2.imwrite("img/Inverse.jpg", inverse_image)

# Plot the inverse image
plt.subplot(1, 2, 2)
plt.title("Inverse color")
plt.imshow(inverse_image)
plt.show()
