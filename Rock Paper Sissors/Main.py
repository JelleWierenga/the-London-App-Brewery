import random

choice: int = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for Scissors.\n"))
computer: int = random.randint(0, 2)

print(f"Computer choose {computer}")

if choice == 0 and computer == 2:
    print("You win")
elif computer == 0 and choice == 2:
    print("You lose")
elif computer > choice:
    print("You lose")
elif choice > computer:
    print("You win")
elif computer == choice:
    print("Draw")
elif choice >= 3 or choice < 0:
    print("Invalid number")