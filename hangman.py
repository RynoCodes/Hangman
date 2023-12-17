# This program is a hangman game created for a discord server. This program uses lists of characters from the DC
# universe and creates a hangman guessing game.

import random


# prints hangman based on incorrect guesses
def print_hangman():
    hangman_0 = """
          -----
              |
              |
              |
              |
              |
              |
        ______|
        |     |"""

    hangman_1 = """
          -----
          |   |
          O   |
              |
              |
              |
              |
        ______|
        |     |"""

    hangman_2 = """
          ------
          |    |
          O    |
         /|\\   |
               |
               |
               |
        _______|
        |      |"""

    hangman_3 = """
          ------
          |    |
          O    |
         /|\\   |
         \\|/   |
               |
               |
        _______|
        |      |"""

    hangman_4 = """
          ------
          |    |
          O    |
         /|\\   |
         \\|/   |
         / \\   |
               |
        _______|
        |      |"""

    hangman_lose = """
              -----
              |   |
              O   |
             /|\\  |
             \\|/  |
             / \\  |
            /   \\ |
            ______|
            |     |"""
# TODO: change to switch/case
    if wrong_guess == 0:
        print(hangman_0)
    elif wrong_guess == 1:
        print(hangman_1)
    elif wrong_guess == 2:
        print(hangman_2)
    elif wrong_guess == 3:
        print(hangman_3)
    elif wrong_guess == 4:
        print(hangman_4)
    elif wrong_guess == 5:
        print(hangman_lose)
    else:
        print("Something went wrong")


# win condition
def win_condition():
    hangman = """
     \\ O /
       |
      / \\
     /   \\"""
    print("Congratulations! You guessed the word: ", word, "\n")
    print(hangman)


# lose condition
def lose_condition():
    hangman_lose = """
              -----
              |   |
              O   |
             /|\\  |
             \\|/  |
             / \\  |
            /   \\ |
            ______|
            |     |"""
    print("Sorry, you lost, the word was: ", word)
    print(hangman_lose)


# selects random word from list
def select_ran(s_list):
    index = random.randint(0, len(s_list))
    return index


# prints word as blanks or guessed letters
def print_blank():
    for x in word:
        if x.isalpha() and x not in guessed_letters:
            print("_", end=" ")
        elif x.isspace():
            print(" ", end=" ")
        else:
            print(x, end="")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # default word list
    word_list = ["BATMAN", "NIGHTWING", "RED HOOD", "RED ROBIN", "SPOILER", "BATGIRL", "BATWOMAN",
                 "AGENT A", "ROBIN", "BLACK BAT", "SIGNAL", "BLUEBIRD", "CATWOMAN", "ORACLE"]
    wrong_guess = 0
    correct_guess = 0
    guessed_letters = []
    word = word_list[select_ran(word_list)]
    # print(word)
    play_game = True

    while play_game:
        print_hangman()
        print_blank()
        guess = input("\nPlease guess a letter\n").upper()
        # check if letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter")
            continue
        # add guess to guessed list
        else:
            guessed_letters.append(guess)
        # increment wrong_guess if guess is wrong, increment correct_guess if guess is correct
        if guess not in word:
            wrong_guess += 1
            print("Sorry,", guess, "is not in the word\n")
        else:
            print(guess, " is correct")
            correct_guess += word.count(guess)
        # win/lose condition
        if correct_guess == len(word.replace(" ", "")) or wrong_guess == 5:
            if correct_guess == len(word.replace(" ", "")):
                win_condition()
            elif wrong_guess == 5:
                lose_condition()

            print("Thank you for playing!")
            user_input = input("Press any key to exit")
            break
