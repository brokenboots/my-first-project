import tkinter as tk
from tkinter import messagebox
import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        json.dump(list(tasks), file)


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty")
        return

    listbox.insert(tk.END, "❌ " + task)
    entry.delete(0, tk.END)

    save_tasks()


def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete")


def complete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if task.startswith("✔"):
            return

        new_task = task.replace("❌", "✔", 1)

        listbox.delete(selected)
        listbox.insert(selected, new_task)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task first")


# Window
window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x450")


# Title
title = tk.Label(window, text="My To-Do List", font=("Arial", 18))
title.pack(pady=10)


# Entry field
entry = tk.Entry(window, width=30)
entry.pack(pady=10)


# Add button
add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)


# Frame for listbox + scrollbar
frame = tk.Frame(window)
frame.pack(pady=20)


scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Task list
listbox = tk.Listbox(frame, width=40, height=10, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)


# Buttons
complete_button = tk.Button(window, text="Mark Completed", width=20, command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)


# Load saved tasks
tasks = load_tasks()

for task in tasks:
    listbox.insert(tk.END, task)


window.mainloop()