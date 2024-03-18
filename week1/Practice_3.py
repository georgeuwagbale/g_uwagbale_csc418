import cv2

import os

image_path = r"C:/Users/DELL/OneDrive\Documents/Year_4/Semester Two/CSC418/g_uwagbale_csc418/week1/img/"

directory = r"C:/Users/DELL/OneDrive\Documents/Year_4/Semester Two/CSC418/g_uwagbale_csc418/week1/img/"

img = cv2.imread(image_path + "lenna.png", 0)

os.chdir(directory)

print("Before saving image: ")
print(os.listdir(directory))

filename = "lenna_gray.png"

cv2.imwrite(filename, img)

print("After saving image: ")
print(os.listdir(directory))

print("Image saved as: ", filename)