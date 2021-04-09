import random
from hangman_art import stages, logo
from hangman_words import word_list
import replit


def HangmanGame():
    print(logo)
    game_is_finished = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []
    wrong_guess = []
    for _ in range(word_length):
        display += "_"

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()

        # Use the clear() function imported from replit to clear the output between guesses.
        replit.clear()

        if guess in display:
            print(f"You've already guessed {guess}")
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

        print(f"{' '.join(display)}\n")

        if guess not in chosen_word:
            if guess in wrong_guess:
                print(f"You have already guessed {guess} and it's wrong guess. So, try to guess other letter.")
            else:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    game_is_finished = True
                    print("You lose.")
            wrong_guess.append(guess)

        if not "_" in display:
            game_is_finished = True
            print("You win.")

        print(stages[lives])


play = True

while play:
    HangmanGame()
    print("Enter q to quit the game or any other letter or word to continue: ")
    a = input()

    if a == 'q' or a == 'Q':
        play = False
    else:
        replit.clear()
        print("let's play again!")
