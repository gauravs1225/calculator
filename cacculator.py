import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Can't divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num2 = tk.Label(root, text="Enter second number:")
label_operation = tk.Label(root, text="Select operation:")

entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar()
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, *operations)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, text="Result: ")

label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()
label_operation.pack()
operation_menu.pack()
calculate_button.pack()
result_label.pack()

root.mainloop()
