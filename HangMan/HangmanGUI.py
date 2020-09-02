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
x = (master.winfo_screenwidth() - master.winfo_reqwidth()) / 2 - 200
y = (master.winfo_screenheight() - master.winfo_reqheight()) / 2 - 200
master.geometry('%dx%d+%d+%d' % (700, 500, x, y))  # 700 500
master.resizable(False, False)

w = Canvas(master, width=700, height=500, bg='#046A38')
w.pack()

w.create_rectangle(40, 200, 60, 460, outline="#000000", fill="#000000")
w.create_rectangle(60, 200, 200, 220, outline="#000000", fill="#000000")
w.create_rectangle(177, 220, 180, 255, outline="#000000", fill="#000000")

guesses = Label(master, text="Guessed Letters", font=("Courier Bold", 14), bg='#046A38', fg="#B9975B")
guesses.place(x="460", y="170")
w.create_rectangle(420, 200, 650, 455, outline="#000000", width="3", fill="#B9975B")
guess_label = Label(master, text="", font=("Courier Bold", 14), bg='#B9975B', wraplength=190, justify=LEFT)  # 1
guess_label.place(x="455", y="205")
letter_guesses = []  # 2

top_lines = Label(master, text=top, font=("Courier", 35), bg="#046A38", fg="#B9975B")  # 3
top_lines.place(x="2", y="4")

label = Label(master, text="Guess a letter:", font=("Courier Bold", 16), bg="#046A38", fg="#B9975B")
label.place(x="35", y="85")

letter_guess = Entry(master, width=4, font=("Courier Bold", 18), justify='center', bg="#B9975B")
letter_guess.place(x="190", y="85")

label2 = Label(master, text="Guess a word:", font=("Courier Bold", 16), bg="#046A38", fg="#B9975B")
label2.place(x="35", y="130")

word_guess = Entry(master, width=10, font=("Courier Bold", 18), bg="#B9975B")
word_guess.place(x="190", y="130")

check_mark = Label(master, text="", font=("Courier Bold", 20), bg="#046A38", fg="light green")  # 4
check_mark.place(x="338", y="124")

incorrect_guesses = []


def button_click():
    guess = letter_guess.get()
    guess_word = word_guess.get()
    letter_guess.delete(0, 'end')
    word_guess.delete(0, 'end')

    if guess not in game_puzzle:
        incorrect_guesses.append(0)

    if guess not in game_puzzle:
        if len(incorrect_guesses) == 1:
            w.create_oval(155, 250, 205, 300, outline="#000000", fill="#ffffff", width="4")
        if len(incorrect_guesses) == 2:
            w.create_rectangle(170, 297, 190, 340, outline="#000000", fill="orange", width="4")
        if len(incorrect_guesses) == 3:
            w.create_line(170, 305, 150, 295, width="6")
        if len(incorrect_guesses) == 4:
            w.create_line(190, 305, 210, 295, width="6")
        if len(incorrect_guesses) == 5:
            w.create_line(173, 340, 170, 365, width="6")
        if len(incorrect_guesses) == 6:
            w.create_line(187, 340, 190, 365, width="6")
            print("YOU LOSE")
            check_mark.config(text="x", fg="red")

            lose_window = Tk()
            lose_window.title('Hang-Man')
            win_canvas = Canvas(lose_window, width=250, height=200, bg='#046A38')
            x_lose = (master.winfo_screenwidth() - lose_window.winfo_reqwidth()) / 2 - 50
            y_lose = (master.winfo_screenheight() - lose_window.winfo_reqheight()) / 2 - 100
            lose_window.geometry('%dx%d+%d+%d' % (250, 200, x_lose, y_lose))  # 700 500
            lose_window.resizable(False, False)
            win_canvas.pack()
            lose_label = Label(lose_window, text="You Lose!", font=("System Bold", 25), bg="#046A38", fg="#B9975B")
            lose_label.place(x="50", y="80")
            letter_guess["state"] = "disabled"
            word_guess["state"] = "disabled"

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
                lines[n] = game_puzzle[n] + " "
            top_lines.config(text=temp)

    # check for victory
    check = ""
    for t in range(word_length):
        check += lines[t]
    check = check.replace(" ", "")
    if check == game_puzzle:
        print("WINNER")
        check_mark.config(text="✔")
        win_window = Tk()
        win_window.title('Hang-Man')
        win_canvas = Canvas(win_window, width=250, height=200, bg='#046A38')
        x_win = (master.winfo_screenwidth() - win_window.winfo_reqwidth()) / 2 - 50
        y_win = (master.winfo_screenheight() - win_window.winfo_reqheight()) / 2 - 100
        win_window.geometry('%dx%d+%d+%d' % (250, 200, x_win, y_win))  # 700 500
        win_window.resizable(False, False)
        win_canvas.pack()
        win_label = Label(win_window, text="You Win!", font=("System Bold", 25), bg="#046A38", fg="#B9975B")
        win_label.place(x="50", y="80")
        letter_guess["state"] = "disabled"
        word_guess["state"] = "disabled"

    print(check)
    print(game_puzzle)


button_guess = Button(master, text="Submit", font=("System Bold", 12), command=button_click)
button_guess.place(x="260", y="85")
mainloop()
