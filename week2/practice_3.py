import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread("img/george.jpg")

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

# Adjust the brightness and contrast
brightness = 5
contrast = 1.5
result_image = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

# Save the image
cv2.imwrite("img/contrast_image.jpg", result_image)

# Plot the contrast image
plt.subplot(1, 2, 2)
plt.title("Brightness & Contrast")
plt.imshow(result_image)
plt.show()

