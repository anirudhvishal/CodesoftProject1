
from tkinter import *

root = Tk()
root.title("SIMPLE CALCULATOR")

my_entry = Entry(root, width=30, borderwidth=5)
my_entry.grid(row=0, column=0, columnspan=4)


def my_click(number):
    current = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, str(current) + str(number))


def my_clear():
    my_entry.delete(0, END)


def perform_operation(operator):
    global f_num
    global current_operation
    current_operation = operator
    first_number = my_entry.get()
    f_num = int(first_number)
    my_entry.delete(0, END)


def calculate_result():
    second_number = my_entry.get()
    my_entry.delete(0, END)
    
    if current_operation == "addition":
        my_entry.insert(0, f_num + int(second_number))
    elif current_operation == "subtraction":
        my_entry.insert(0, f_num - int(second_number))
    elif current_operation == "division":
        my_entry.insert(0, f_num / int(second_number))
    elif current_operation == "multiplication":
        my_entry.insert(0, f_num * int(second_number))



buttons_layout = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "CLR", "=", "/"]
]

for i, row in enumerate(buttons_layout):
    for j, button_text in enumerate(row):
        button = Button(root, text=button_text, padx=30, pady=10)
        
        if button_text.isdigit() or button_text == "CLR":
            button.configure(command=lambda text=button_text: my_click(text))
        elif button_text in ("+", "-", "*", "/"):
            button.configure(command=lambda op=button_text: perform_operation(op))
        elif button_text == "=":
            button.configure(command=calculate_result)

        button.grid(row=i + 1, column=j)

root.mainloop()
