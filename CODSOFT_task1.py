import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
DATA_FILE = 'task_data.json'
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
def add_new_task():
    task_description = simpledialog.askstring("Add Task", "Enter the task description:")
    if task_description:
        tasks_list.append({'description': task_description, 'is_done': False})
        save_data(tasks_list)
        refresh_task_list()
def modify_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Modify Task", "No task selected.")
        return
    index = selected_index[0]
    new_description = simpledialog.askstring("Modify Task", "Enter the new task description:")
    if new_description:
        tasks_list[index]['description'] = new_description
        save_data(tasks_list)
        refresh_task_list()
def remove_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Remove Task", "No task selected.")
        return
    index = selected_index[0]
    tasks_list.pop(index)
    save_data(tasks_list)
    refresh_task_list()
def complete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Complete Task", "No task selected.")
        return
    index = selected_index[0]
    tasks_list[index]['is_done'] = True
    save_data(tasks_list)
    refresh_task_list()
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks_list:
        status = "Completed" if task['is_done'] else "Pending"
        task_listbox.insert(tk.END, f"{task['description']} [{status}]")
root = tk.Tk()
root.title("Task Manager")
tasks_list = load_data()
btn_add = tk.Button(root, text="Add Task", command=add_new_task)
btn_add.pack(pady=5)
btn_modify = tk.Button(root, text="Modify Task", command=modify_task)
btn_modify.pack(pady=5)
btn_remove = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove.pack(pady=5)
btn_complete = tk.Button(root, text="Complete Task", command=complete_task)
btn_complete.pack(pady=5)
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)
refresh_task_list()
root.mainloop()
