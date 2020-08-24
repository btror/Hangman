from random import randrange


def generate_puzzle():
    potential_puzzles = ['fredrick', 'brandon', 'minecraft', "charlotte", 'washington', 'vermont', 'fortnite']
    random = randrange(0, 7)
    puzzle = potential_puzzles[random]
    return puzzle


game_puzzle = generate_puzzle()


def start_game():
    word_length = 0
    lines = []
    for i in range(len(game_puzzle)):
        word_length += 1
        lines.append(' _')

    attempts = 0
    while True:
        print("***** Incorrect Guesses:", attempts, "*****")
        if attempts == 0:
            start = ''
            for i in range(len(game_puzzle)):
                start += ' _ '
            print(start)

        guess = input("Guess a letter: ")
        print("Your guess:", guess)

        locations = []
        index = -1
        letter_found = False
        while True:
            index = game_puzzle.find(guess, index + 1)
            if index == -1:
                break
            locations.append(index)
            lines[index] = guess
            letter_found = True

        if not letter_found:
            attempts += 1

        print(' '.join(lines))

        solve = input("Solve puzzle? (y/n): ")
        if solve == 'y':
            guess = input("Guess the word: ")
            if guess == game_puzzle:
                print("Correct! You win!")
                break

        if attempts == 9:
            print("You lose!")
        print("\n")


start_game()
