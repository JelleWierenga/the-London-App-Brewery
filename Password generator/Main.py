import random

print("Welcome to the PyPassword Generator!")
letter_input: int = int(input("How many letters would you like in your password?\n"))
symbols_input: int = int(input("How many symbols would you like?\n"))
numbers_input: int = int(input("HOw many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

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