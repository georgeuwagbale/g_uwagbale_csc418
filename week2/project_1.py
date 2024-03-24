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
            print("3. Visualize Color Spaces")
            print("4. Arithmetic operation on images")
            print("5. Sharpen image")
            print("6. Remove noise")
            print("7. Image scaling")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                enhanced_image = brightness_and_contrast_enhancement(image, 1.5, 1.5)
            elif choice == 2:
                enhanced_image = inverse_transform(image)
            elif choice == 3:
                visualize_color_space(image)
            elif choice == 4:
                add_two_images(image, cv2.imread("./img/punch.jpg"))
            elif choice == 5:
                sharpen_image(image)
            elif choice == 6:
                remove_noise(image)
            elif choice == 7:
                scale_image(image)
            else:
                print("Invalid option")


def visualize_color_space(image: np.ndarray):
    # The split method separates color spaces
    B, G, R = cv2.split(image)

    # Corresponding channels are separated
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    cv2.imshow("Blue", B)
    cv2.waitKey(0)

    cv2.imshow("Green", G)
    cv2.waitKey(0)

    cv2.imshow("Red", R)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

def brightness_and_contrast_enhancement(image: np.ndarray, brightness: float, contrast: float) -> np.ndarray:
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)

    result_image = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

    # Save the image
    cv2.imwrite("img/contrast_image.jpg", result_image)

    # Plot the contrast image
    plt.subplot(1, 2, 2)
    plt.title("Brightness & Contrast")
    plt.imshow(result_image)
    plt.show()


def inverse_transform(image: np.ndarray) -> None:
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

def sharpen_image(image: np.ndarray) -> None:
    # Plot the original image
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)

    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Sharpen the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Save the image
    cv2.imwrite('img/sharpened_image.jpg', sharpened_image)

    # Plot the sharpened image
    plt.subplot(1, 2, 2)
    plt.title("Sharpened Image")
    plt.imshow(sharpened_image)
    plt.show()


def scale_image(image: np.ndarray, scale_factor: float) -> None:
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)

    # Scale the image by a factor of 2 along both axes
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

    # Save the image
    cv2.imwrite("img/Scaled.jpg", scaled_image)

    # Plot the scaled image
    plt.subplot(1, 2, 2)
    plt.title("Scaled Image")
    plt.imshow(scaled_image)
    plt.show()


def add_two_images(image_1: np.ndarray, image_2: np.ndarray) -> None:
    # Resize images
    image1 = cv2.resize(image_1, (500, 400))
    image2 = cv2.resize(image_2, (500, 400))

    # Add the images
    added_image = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)

    # sub = cv2.subtract(image1, image2)

    # Display the added image
    cv2.imshow('Added Image', added_image)

    # De-alloacte any associated memory usage
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

def remove_noise(image: np.ndarray) -> None:
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


username = input("Enter your username: ")
mat_no = input("Enter your matric no: ")

login(username, mat_no)