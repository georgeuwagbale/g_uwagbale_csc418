import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
  

database = [
    {"username": "Anderson", "mat_no": "20133529334", "image": "img/anderson.jpg"},
    {"username": "Chimaje", "mat_no": "20133529335", "image": "img/chimaje.jpg"},
    {"username": "David", "mat_no": "20133529336", "image": "img/david.jpg"},
    {"username": "Desmond", "mat_no": "20133529337", "image": "img/desmond.jpg"},
    {"username": "George", "mat_no": "20133529338", "image": "img/george.jpg"},
    {"username": "Kobi", "mat_no": "20133529339", "image": "img/kobi.jpg"},
    {"username": "Lala", "mat_no": "20133529340", "image": "img/lala.jpg"},
    {"username": "Lotanna", "mat_no": "20133529341", "image": "img/lotanna.jpg"},
    {"username": "Punch", "mat_no": "20133529342", "image": "img/punch.jpg"},
    {"username": "Zion", "mat_no": "20133529343", "image": "img/zion.jpg"}
]


def login (username: str, mat_no: str) -> None:
    for user in database:
        if user["username"] == username and user["mat_no"] == mat_no:
            print("Logged in successfully\nWelcome to the system")
            # Load the image
            image = cv2.imread(user["image"])
            enhanced_image = None
            print("\nWhat transformation do you want: ")
            print("1. Brightness and Contrast Enhancement\n2. Inverse Transformation")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                enhanced_image = brightness_and_contrast_enhancement(image, 1.5, 1.5)
            elif choice == 2:
                enhanced_image = inverse_transform(image)

            # Plot the original image
            plt.subplot(1, 2, 1)
            plt.title("Original Image")
            plt.imshow(image)

            # Save the image
            cv2.imwrite("img/enhanced.jpg", enhanced_image)

            # Plot the enhanced image
            plt.subplot(1, 2, 2)
            plt.title("Enhanced Image")
            plt.imshow(enhanced_image)
            plt.show()


def brightness_and_contrast_enhancement(image: np.ndarray, brightness: float, constrast: float) -> np.ndarray:
    result_image = cv2.addWeighted(image,  constrast, np.zeros(image.shape, image.dtype), 0, brightness)
    return result_image

def inverse_transform(image: np.ndarray) -> np.ndarray:
    inverse_image = 255 - image
    return inverse_image

def sharpen_image(image: np.ndarray) -> np.ndarray:
    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # Sharpen the image
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

def scale_image(image: np.ndarray, scale_factor: float) -> np.ndarray:
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    return scaled_image
