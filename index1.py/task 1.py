#task 1

import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task before adding!")

def delete_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        tasks.remove(selected_task)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index] = tasks[index] + " ✅"
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task to mark done!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10, selectmode=tk.SINGLE)
listbox.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark Done", command=mark_done)
done_button.pack(pady=5)

root.mainloop()