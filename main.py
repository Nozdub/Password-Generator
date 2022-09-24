#------------------------------------------ PASSWORD GENERATOR --------------------------------------------------------#
import random
import string
import tkinter as tk
import PyPDF2



intro = "-------------- Welcome to Nozdub's password generator! --------------"
print(intro)

# Text file I found online containing a large amount of words, it will be used to select random words to use in the pw.
file = open("words_alpha.txt", "r")
word_list = list(file.read().split("\n"))


wip_password = []


# Function that takes integer user input on how many words, symbols and numbers and appends a random selection to a
# list, then it shuffles them.

def generate_password():
    for i in range (int(input(f"How many words would you like your password to contain? "))):
        part_one = random.choice(word_list)
        wip_password.append(part_one)

    for s in range (int(input(f"How many symbols would you like your password to contain? "))):
        symbols = ["@", "|", "#", "£", "$", "-", "_"]
        part_two = random.choice(symbols)
        wip_password.append(part_two)

    for n in range (int(input(f"How many numbers would you like your password to contain? "))):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        part_two = random.choice(numbers)
        wip_password.append(part_two)

    random.shuffle(wip_password)

    completed_password = "".join(map(str, wip_password))
    print(f"Here is your new password: {completed_password}")


generate_password()

