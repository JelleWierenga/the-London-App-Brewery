import random
from Cards import card_values

user_hand = []
computer_hand = []

def deal_initial_hands():
    for user in range(2):
        user_hand.append(random.choice(list(card_values.keys())))
    for computer in range(2):
        computer_hand.append(random.choice(list(card_values.keys())))
