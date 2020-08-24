from tkinter import *
from random import randrange
from tkinter import Button


def generate_puzzle():
    potential_puzzles = ['fredrick', 'brandon', 'minecraft', "charlotte", 'washington', 'vermont', 'fortnite']
    random = randrange(0, 7)
    puzzle = potential_puzzles[random]
    return puzzle


game_puzzle = generate_puzzle()
lines = []
word_length = 0
top = ''
for i in range(len(game_puzzle)):
    word_length += 1
    lines.append('_ ')
    top += '_ '

master = Tk()
master.title('Hang-Man')
master.geometry("700x500")

top_lines = Label(master, text=top, font=("Courier", 32))
top_lines.pack()

label = Label(master, text="Guess a letter:", font=("Courier", 16))
label.place(x="165", y="75")

letter_guess = Entry(master, width=3, font=("Courier", 18))
letter_guess.place(x="375", y="75")

attempts = 0


def button_click():
    guess = letter_guess.get()
    print(guess)
    index = -1
    locations = []
    letter_found = False
    while True:
        index = game_puzzle.find(guess, index + 1)
        if index == -1:
            break
        locations.append(index)
        lines[index] = guess + " "
        letter_found = True
    x = ' '
    for k in range(word_length):
        x += (lines[k])

    top_lines.config(text=x)


button_guess = Button(master, text="Submit", font=("Courier", 11), command=button_click)
button_guess.place(x="440", y="75")

mainloop()
