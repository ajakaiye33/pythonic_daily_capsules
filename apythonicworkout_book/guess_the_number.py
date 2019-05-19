
import random


def guess_number():
    """
    A program that chosses a random integer between 0 and 100(inclusive)
    then ask the user to guess what the number has chosen
    Each time the user enters a guess, the program indicate one of:
    Too high, Too low, Just right
    If the user guessed correctly, then the program exits. Otherwise the user is
    asked to try again. the program only exit after the user guesses correctly
    """
    guessing_machine = random.randint(1, 101)
    guess_counter = 0

    while True:
        user_answer = int(input("Guess a number between 1 and 100 > "))

        if user_answer == guessing_machine:
            print(f"Just right, {user_answer} is correct")
            play_again = input("would want to play again? [y/n]")
            if play_again == "y":
                continue
            else:
                break

        elif user_answer < guessing_machine:
            print(f"{user_answer} is Too low, {5 - guess_counter} guesse(s) to go")
            guess_counter += 1
            if guess_counter > 3:
                break
            else:
                continue

        elif user_answer > guessing_machine:
            print(f"{user_answer}, is Too high, { 5 - guess_counter} guesse(s) to go")
            guess_counter += 1
            if guess_counter > 5:
                break
            else:
                continue


print(guess_number())
