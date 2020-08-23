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
        lines.append('_ ')
    print(' '.join(lines))

    while True:
        guess = input("Guess a letter: ")
        print("Your guess:", guess, "\n")

        locations = []
        index = -1
        while True:
            index = game_puzzle.find(guess, index + 1)
            if index == -1:
                break
            locations.append(index)
            lines[index] = guess

        print(' '.join(lines))


start_game()
