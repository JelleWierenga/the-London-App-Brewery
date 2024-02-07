import random

compares = {
    "Alice": 1200,
    "Bob": 800,
    "Charlie": 1500,
    "David": 600
}


score = 0

while True:
    random_person = random.choice(list(compares.keys()))
    random_person2 = random.choice(list(compares.keys()))

    while random_person2 == random_person:
        random_person2 = random.choice(list(compares.keys()))

    print(f"{random_person} vs {random_person2}")

    guess = input(f"Does {random_person2} have more or less followers than {random_person}? Type 'more' or 'less': ")

    if guess == "more" and compares[random_person] < compares[random_person2]:
        print("You got it")
        score += 1
    elif guess.lower() == 'less' and compares[random_person] > compares[random_person2]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print(f"Your current score is: {score}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print(f"You ended with {score} points")
        break