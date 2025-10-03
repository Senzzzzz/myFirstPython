import math
import time
import random
import string

import random

hangman_stages = {
    0: (
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
        "======="
    ),
    1: (
        "       ",
        "   O   ",
        "       ",
        "       ",
        "       ",
        "======="
    ),
    2: (
        "       ",
        "   O   ",
        "   |   ",
        "       ",
        "       ",
        "======="
    ),
    3: (
        "       ",
        "   O   ",
        "  /|   ",
        "       ",
        "       ",
        "======="
    ),
    4: (
        "       ",
        "   O   ",
        "  /|\\ ",
        "       ",
        "       ",
        "======="
    ),
    5: (
        "       ",
        "   O   ",
        "  /|\\ ",
        "  /    ",
        "       ",
        "======="
    ),
    6: (
        "       ",
        "   O   ",
        "  /|\\ ",
        "  / \\ ",
        "       ",
        "======="
    ),
}


def display_hangman(stages):
    for stages in hangman_stages[stages]:
        print(stages)


def display_wrong_guesses(guess, word, wrong_guesses):
    if guess not in word:
        wrong_guesses += 1
    return wrong_guesses


def display_result(word, hints):
    if word == hints:
        print(f"You Win! The correct word was: {''.join(word)}")
        return True


def main():
    words = ("apple", "orange", "banana", "coconut", "pomelo", "watermelon")
    word = random.choice(words)
    word = list(word)
    hints = ["_"] * len(word)
    wrong_guesses = 0
    print(" ".join(word))

    while True:
        display_hangman(wrong_guesses)
        guess = input("Enter a letter: ").lower()

        if len(guess) > 1 or not guess.isalpha():
            print("Please type 1 letter")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hints[i] = guess
        print(" ".join(hints))

        wrong_guesses = display_wrong_guesses(guess, word, wrong_guesses)

        if wrong_guesses == 7:
            print("Maximum guesses reached")
            break
        if display_result(word, hints) == True:
            break


if __name__ == "__main__":
    main()
