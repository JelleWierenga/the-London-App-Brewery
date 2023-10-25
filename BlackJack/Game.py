import random
from Cards import card_values
from SetUp import user_hand, computer_hand, deal_initial_hands

def calculate_hand_value(hand):
    total_value = sum(card_values[card] for card in hand)
    ace_count = hand.count("Ace of Hearts")
    while ace_count > 0 and total_value > 21:
        total_value -= 10
        ace_count -= 1
    return total_value

def display_hand(hand, owner):
    print(f"{owner}'s hand:")
    for card in hand:
        print(card)
    print(f"Total value: {calculate_hand_value(hand)}")

def game():
    deal_initial_hands()
    user_hand_value = calculate_hand_value(user_hand)

    print("Initial hands:")
    display_hand(user_hand, "Player")
    display_hand(computer_hand, "Computer")

    if user_hand_value == 21:
        print("Blackjack! You won")
    elif user_hand_value > 21:
        print("You busted. You lose")
    else:
        answer = input("Do you want another card? Type 'y' for yes, 'n' for no: ")
        if answer == "y":
            new_card = random.choice(list(card_values.keys()))
            user_hand.append(new_card)
            print(f"You drew: {new_card}")
            print("Updated hand:")
            display_hand(user_hand, "Player")
            game()
        elif answer == "n":
            computer_hand_value = calculate_hand_value(computer_hand)

            while computer_hand_value < 17:
                new_card = random.choice(list(card_values.keys()))
                computer_hand.append(new_card)
                print(f"Computer drew: {new_card}")

                computer_hand_value = calculate_hand_value(computer_hand)

            print("Final hands:")
            display_hand(user_hand, "Player")
            display_hand(computer_hand, "Computer")

            if computer_hand_value > 21 or user_hand_value > computer_hand_value:
                print("You win")
            elif user_hand_value == computer_hand_value:
                print("Draw")
            else:
                print("You lose")

game()
