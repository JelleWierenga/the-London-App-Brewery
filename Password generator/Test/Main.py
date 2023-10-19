import random
import json

print("Welcome to the PyPassword Generator!")

with open("characters.json", "r") as file:
    characters_data = json.load(file)

letters = characters_data["letters"]
numbers = characters_data["numbers"]
symbols = characters_data["symbols"]

letter_input = int(input("How many letters would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like?\n"))

Temp_store = ""
for letter in range(letter_input):
    get_letter = random.choice(letters)
    Temp_store = Temp_store + get_letter
for symbol in range(symbols_input):
    get_symbol = random.choice(symbols)
    Temp_store = Temp_store + get_symbol
for number in range(numbers_input):
    get_number = random.choice(numbers)
    Temp_store = Temp_store + get_number

Password = list(Temp_store)
random.shuffle(Password)
print("Your generated password is:", ''.join(Password))
