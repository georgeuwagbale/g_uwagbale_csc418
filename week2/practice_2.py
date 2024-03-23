import cv2

# Path to input images
image1 = cv2.imread('img/sst.jpg')
image2 = cv2.imread('img/Model-82A1-29-BBL-MP.png')

# Resize images
image1 = cv2.resize(image1, (500, 400))
image2 = cv2.resize(image2, (500, 400))

# Add the images
added_image = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)

# sub = cv2.subtract(image1, image2)

# Display the added image
cv2.imshow('Added Image', added_image)

# De-alloacte any associated memory usage
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()