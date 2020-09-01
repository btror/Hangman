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
    if i == 0:
        top += ' _ '
    if i > 0:
        top += '_ '

master = Tk()
master.title('Hang-Man')
master.geometry("700x500")
master.resizable(False, False)

w = Canvas(master, width=700, height=500, bg='red')
w.pack()

w.create_rectangle(40, 200, 60, 460, outline="#000000", fill="#000000")
w.create_rectangle(60, 200, 200, 220, outline="#000000", fill="#000000")
w.create_rectangle(175, 220, 180, 255, outline="#000000", fill="#000000")

guesses = Label(master, text="Guessed Letters", font=("Courier Bold", 14), bg='red')
guesses.place(x="460", y="170")
w.create_rectangle(420, 200, 650, 455, outline="#000000", width="3")
guess_label = Label(master, text="", font=("Courier Bold", 14), bg='red', wraplength=190, justify=LEFT)
guess_label.place(x="455", y="205")
letter_guesses = []

top_lines = Label(master, text=top, font=("Courier", 32))
top_lines.place(x="10", y="10")

label = Label(master, text="Guess a letter:", font=("Courier", 16))
label.place(x="10", y="75")

letter_guess = Entry(master, width=4, font=("Courier", 18), justify='center')
letter_guess.place(x="220", y="75")

label2 = Label(master, text="Guess the word:", font=("Courier", 16))
label2.place(x="10", y="120")

word_guess = Entry(master, width=10, font=("Courier", 18))
word_guess.place(x="220", y="120")


def button_click():
    guess = letter_guess.get()
    guess_word = word_guess.get()
    letter_guess.delete(0, 'end')
    word_guess.delete(0, 'end')

    if len(guess) > 0:
        index = -1
        locations = []
        while True:
            index = game_puzzle.find(guess, index + 1)
            if index == -1:
                break
            locations.append(index)
            lines[index] = guess + " "
        if guess not in letter_guesses and len(guess) == 1:
            temp = guess_label['text']
            temp += '' + guess + '            '
            guess_label.config(text=temp)
            letter_guesses.append(guess)

        x = ' '
        for k in range(word_length):
            x += (lines[k])
        top_lines.config(text=x)
    if len(guess_word) > 0:
        if guess_word == game_puzzle:
            temp = ''
            for n in range(word_length):
                if n > 0:
                    temp += game_puzzle[n] + ' '
                if n == 0:
                    temp += ' ' + game_puzzle[n] + ' '
            top_lines.config(text=temp)


button_guess = Button(master, text="Submit", font=("Courier", 11), command=button_click)
button_guess.place(x="295", y="75")
mainloop()
