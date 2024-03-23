import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("img/lala.jpg")

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

# Scale the image by a factor of 2 along both axes
scaled_image = cv2.resize(image, None, fx=2, fy=2)

# Save the image
cv2.imwrite("img/Scaled.jpg", scaled_image)

# Plot the scaled image
plt.subplot(1, 2, 2)
plt.title("Scaled Image")
plt.imshow(scaled_image)
plt.show()
