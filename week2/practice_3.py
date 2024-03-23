import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread("img/sst.jpg")

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

# Adjust the brightness and contrast
brightness = 5
contrast = 1.5