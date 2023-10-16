print("Welcome to treasure island.\nYour mission is to find the treasure.")
road_cross: str = input("You're at a cross road. Where do you want to go? Type left or right\n").lower()

if road_cross == "left":
    lake_choice: str = input("You came to a lake. There is an island in the middle of the lake. Type wait to wait for "
                             "a boat. type swim to swim across.\n").lower()
    if lake_choice == "wait":
        island_color_choice: str = input("You arrive at the island unharmed. There is a house with 3 doors. One red, "
                                         "one yellow and one blue. Which color do you chose?\n").lower()
        if island_color_choice == "blue":
            print("You enter a room of monsters. Game over")
        elif island_color_choice == "red":
            print("You found a treasure chest. You won!")
        else:
            print("The room is empty. Game over!")
    else:
        print("You chose to swim across, that was not smart. you stumble across some sharks and got eaten. Game over")
# Forest choice
else:
    forest_choice: str = input("You came to a dark forest. There is a cave in the middle of the forest. Type in to go "
                               "in the cane. Type leave to leave.").lower()
    if forest_choice == "in":
        cave_choice: str = input("You entered the cave, you see a cliff. Type jump to jump over it. Type leave to "
                                 "leave the cave").lower()
        if cave_choice == "jump":
            print("You jumped and found a treasure chest. Yay you won")
        else:
            print("You left the cave and stumbled across some angry bats. Game over")
    else:
        print("You did not go in the cave and got taken prisoner by some trolls. Game over")
