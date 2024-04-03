import tkinter as tk
from tkinter import Button
from tkinter import Entry

user_database = [
    {"username": "uwagbalegeorge", "email": "uwagbalegeorge@gmail.com", "password": "password", "age": 22}
]

window = tk.Tk()
window.title("My First GUI Program")
# window.geometry("400x400")
window.resizable(False, False)

tk.Label(window, text="Username").grid(row=1, column=0)
username = Entry(window, width=30)
username.grid(row=1, column=1)

tk.Label(window, text="Password").grid(row=2, column=0)
password = Entry(window, width=30)
password.grid(row=2, column=1)


def login():
    for user in user_database:
        if user.get("username") == username.get() and user.get("password") == password.get():
            print("user logged in successfully!!")
            return True

    print("Incorrect email or password")
    


Button(window, text="Login", width=30, command=login).grid(row=3, column=1)


window.mainloop()
