import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please Enter The Task")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)


root = tk.Tk()
root.geometry('500x450+500+200')
root.title('To Do List App')
root.config(bg='black')
root.resizable(width=True, height=True)


frame = tk.Frame(root)
frame.pack(pady=20)


listbox = tk.Listbox(
    frame,
    height=8,
    width=40,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=10,
    selectbackground='gray',
    activestyle='none',
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

tasks = [
    'Finish HW',
    'Drink water',
    'Write software',
    'Take a nap',
    'Learn something',
    'Write code',
]

for item in tasks:
    listbox.insert(tk.END, item)


scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


entry = tk.Entry(
    root,
    font=('Times', 14)
)
entry.pack(pady=20)


button_frame = tk.Frame(root)
button_frame.pack(pady=20)


add_button = tk.Button(
    button_frame,
    text='Add Task',
    font=('Times', 14),
    bg='white',
    padx=20,
    pady=10,
    command=add_task
)
add_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)


delete_button = tk.Button(
    button_frame,
    text='Delete Task',
    font=('Times', 14),
    bg='white',
    padx=20,
    pady=10,
    command=delete_task
)
delete_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)


root.mainloop()
