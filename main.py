import tkinter as tk
from tkinter import messagebox
import os

# 1. وظائف التعامل مع الملفات
FILE_NAME = "routine.txt"

def save_to_file(task_text):
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(task_text + "\n")

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                routine_list.insert(tk.END, line.strip())

# 2. إعداد النافذة
root = tk.Tk()
root.title("Smart Routine Generator Pro")
root.geometry("400x550")
root.configure(bg="#f0f0f0")

# 3. وظيفة الإضافة
def add_task():
    task = task_entry.get()                 
    time = time_entry.get()
    
    if task != "" and time != "":
        full_line = f"🕒 {time} - {task}"
        routine_list.insert(tk.END, full_line)
        save_to_file(full_line)
        task_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please fill in both fields!")

# 4. وظيفة المسح
def clear_list():
    if messagebox.askyesno("Confirm", "Delete all tasks and clear history?"):
        routine_list.delete(0, tk.END)
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)

# 5. الواجهة
tk.Label(root, text="Smart Routine Pro", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

tk.Label(root, text="Task:", bg="#f0f0f0").pack()
task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=5)

tk.Label(root, text="Time (e.g. 09:00 AM):", bg="#f0f0f0").pack()
time_entry = tk.Entry(root, width=35, font=("Arial", 12))
time_entry.pack(pady=5)

add_button = tk.Button(root, text="Add & Save Task", command=add_task, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=20)
add_button.pack(pady=15)

tk.Label(root, text="Saved Daily Schedule:", bg="#f0f0f0", font=("Arial", 10, "italic")).pack()
routine_list = tk.Listbox(root, width=45, height=12, font=("Arial", 11), bd=2)
routine_list.pack(pady=5, padx=10) # تم تصحيح الخطأ هنا من px لـ padx

clear_button = tk.Button(root, text="Clear All History", command=clear_list, bg="#e74c3c", fg="white", font=("Arial", 9))
clear_button.pack(pady=10)

load_tasks()
root.mainloop()