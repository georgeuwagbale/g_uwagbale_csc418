import cv2

path = "img/eze.jpg"

# The second argument is the color mode
img = cv2.imread(path, 0)

window_name = "Image"

# The first argument is the window name
# The second argument is the image
cv2.imshow(window_name, img)

# The argument is the time in milliseconds to wait for a key press
cv2.waitKey(0)

cv2.destroyAllWindows()