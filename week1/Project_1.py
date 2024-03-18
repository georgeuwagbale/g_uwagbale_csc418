import cv2

database = [
    {"username": "gideon", "password": "6"},
    {"username": "akindayo", "password": "8"},
    {"username": "desmond", "password": "4"}
]


def login(username: str, password: str) -> None:

    for user in database:
        if user["username"] == username and user["password"] == password:
            path: str = "img/" + username + ".png"
            window_name: str = f"{username}'s Successfully logged In"

            img = cv2.imread(path, 1)
            if img is None:
                return "Image not found"
            
            cv2.imshow(window_name, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        

    

    


    
