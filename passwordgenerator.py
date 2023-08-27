import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
        else:
            password = generate_password(length)
            password_label.config(text="Generated password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter desired password length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
password_label = tk.Label(root, text="Generated password: ")

length_label.pack()
length_entry.pack()
generate_button.pack()
password_label.pack()

root.mainloop()
