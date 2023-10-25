import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type easy or hard: ")


def easy_game():
    attempts = 10
    easy_number = random.randint(0, 101)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess: int = int(input("Make a guess: "))
        attempts = attempts - 1
        if easy_number < guess:
            print("To High")
        elif easy_number > guess:
            print("To Low")
        else:
            print(f"You won with {attempts} attempts left")
            break

def hard_game():
    attempts = 5
    hard_number = random.randint(0, 101)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess: int = int(input("Make a guess: "))
        attempts = attempts - 1
        if hard_number < guess:
            print("To High")
        elif hard_number > guess:
            print("To Low")
        else:
            print(f"You won with {attempts} attempts left")
            break


if choose_difficulty == "easy":
    easy_game()
elif choose_difficulty == "hard":
    hard_game()
else:
    print("Not a valid input")