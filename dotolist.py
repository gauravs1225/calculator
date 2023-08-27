import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return "Task added: " + task

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return "Task removed: " + task
        else:
            return "Task not found."

    def get_tasks(self):
        if self.tasks:
            return "\n".join(self.tasks)
        else:
            return "No tasks yet."

def add_task_button_click():
    task = task_entry.get()
    if task:
        result = todo_list.add_task(task)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showerror("Error", "Task cannot be empty.")

def remove_task_button_click():
    task = task_entry.get()
    if task:
        result = todo_list.remove_task(task)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showerror("Error", "Task cannot be empty.")

def update_task_list():
    task_list_text.config(state=tk.NORMAL)
    task_list_text.delete("1.0", tk.END)
    task_list_text.insert(tk.END, todo_list.get_tasks())
    task_list_text.config(state=tk.DISABLED)

todo_list = ToDoList()

root = tk.Tk()
root.title("To-Do List Application")

task_label = tk.Label(root, text="Enter task:")
task_entry = tk.Entry(root)
add_task_button = tk.Button(root, text="Add Task", command=add_task_button_click)
remove_task_button = tk.Button(root, text="Remove Task", command=remove_task_button_click)
task_list_label = tk.Label(root, text="Tasks:")
task_list_text = tk.Text(root, state=tk.DISABLED)

task_label.pack()
task_entry.pack()
add_task_button.pack()
remove_task_button.pack()
task_list_label.pack()
task_list_text.pack()

root.mainloop()
