import random
from word_list import words
from display import draw


# play hangman

def play():

    # select random word from list of words

    word = random.choice(words).upper()

    # initialize variables

    progress = "_" * len(word)
    complete = False
    guessed_words = []
    guessed_letters = []
    attempts_left = 6

    # print information before first game

    print("\n")
    print("HANGMAN")
    print("Start Game")
    print(draw(attempts_left))
    print(progress)
    while not complete and attempts_left > 0:

        # start guessing

        guess = input("Guess a letter or word: ").upper()
        print("\n")

        # if guess is a letter

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You have already guessed the letter, "{guess}".')
            elif guess not in word:
                attempts_left -= 1
                print(f'Incorrect guess! "{guess}" is not in the word.')
                guessed_letters.append(guess)
            else:
                print(f'Good guess! "{guess}" is in the word.')
                guessed_letters.append(guess)

                # modifying progress to include correctly guessed letters

                progress_list = list(progress)
                word_list = list(word)

                for i in range(0, len(word)):
                    if guess == word_list[i]:
                        progress_list[i] = guess
                progress = "".join(progress_list)

                # checking if the word is now complete

                if "_" not in progress:
                    complete = True

        # if guess is a word with length = len(word)

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You have already guessed the word, "{guess}".')
            elif guess != word:
                attempts_left -= 1
                print(f'Incorrect guess! "{guess}" is not the word.')
                guessed_words.append(guess)
            else:
                progress = word
                complete = True

        # invalid inputs

        else:
            print(f'"{guess}" is an INVALID GUESS. Try again.')

        # print new hangman

        print(draw(attempts_left))
        print(progress)

    print("\n")

    # printing winning/losing message

    if complete:
        print("Congrats! You guessed the correct word!\nYOU WIN!!!")
    else:
        print(f'GAME OVER! You ran out of tries.\nThe word was {word}.')

    print("\n")


def main():

    play()

    # looping play() if player wants to play again

    while input("Play Again? ('Y'/'N') ").upper() == "Y":
        play()


if __name__ == "__main__":
    main()
