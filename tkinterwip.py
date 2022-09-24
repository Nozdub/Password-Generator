import string
from tkinter.ttk import Label

import PyPDF2
import tkinter as tk

import self as self
from PIL import Image, ImageTk
import random
from tkinter import messagebox

intro = "-------------- Welcome to Nozdub's password generator! --------------"
print(intro)

# Text file I found online containing a large amount of words, it will be used to select random words to use in the pw.
file = open("words_alpha.txt", "r")
word_list = list(file.read().split("\n"))

wip_password = []
#adding note

def generate_password():
    for i in range(int(e1.get())):
        part_one = random.choice(word_list)
        wip_password.append(part_one)

    for s in range(int(e2.get())):
        symbols = ["@", "|", "#", "£", "$", "-", "_"]
        part_two = random.choice(symbols)
        wip_password.append(part_two)

    for n in range(int(e3.get())):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        part_three = random.choice(numbers)
        wip_password.append(part_three)

    random.shuffle(wip_password)

    completed_password = "".join(map(str, wip_password))
    print(completed_password)
    return completed_password


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=5, rowspan=5)

# Labels
tk.Label(root, text='How many words would you like your password to contain?', font="Calibri").grid(row=1)
tk.Label(root, text='How many symbols would you like your password to contain?', font="Calibri").grid(row=2)
tk.Label(root, text='How many numbers would you like your password to contain?', font="Calibri").grid(row=3)

# Entry field
e1 = tk.Entry(root, width=7)
e2 = tk.Entry(root, width=7)
e3 = tk.Entry(root, width=7)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)


# create button

def print_text(text):
    password_label = tk.Label(root, text=text, font=("Calibri"))
    password_label.grid(row=5, column=0)
    return password_label


b1 = tk.Button(root, text="Create Password", command=lambda: print_text(f"{generate_password()}"), font="Calibri",
               fg="black", height=1, width=20)
b1.grid(row=4, column=0)
b1.update()


canvas = tk.Canvas(root, width=600, height=100)
canvas.grid(columnspan=3, rowspan=5)

root.mainloop()
