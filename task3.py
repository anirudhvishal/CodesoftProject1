import random
from tkinter import *

def generate_password():
    try:
        length = int(entry.get())
        password = "".join(random.sample(combine, length))
        label_2.config(text="Generated Password: " + password)
    except ValueError:
        label_2.config(text="Please enter a valid number")

root = Tk()
root.title("Password Generator")
root.geometry('300x400')

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
num = "0123456789"
sym = "!@#$%^&*()+=_-"
combine = alp + num + sym

label = Label(root, text="No Of Characters")
label.pack()

entry = Entry(root, width=20)
entry.pack()

button = Button(root, text="Generate Password", command=generate_password)
button.pack()

label_2 = Label(root)
label_2.pack()

root.mainloop()
