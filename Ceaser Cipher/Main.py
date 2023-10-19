alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

en_or_de: str = str(input("Type 'encode' to encrypt, type 'decode' to decrypt\n")).lower()
message: str = str(input("Type your message:\n")).lower()
shift_number: int = int(input("Type the shift number:\n"))

def encrypt(message, shift_number):
    encoded = ""
    for index in range(len(message)):
        value = alphabet.index((message[index]))
        value = value + shift_number
        encoded = encoded + alphabet[value]
    print(f"Here is your {en_or_de}d message: {encoded}")


def decrypt(message, shift_number):
    decoded = ""
    for index in range(len(message)):
        value = alphabet.index((message[index]))
        value = value - shift_number
        decoded = decoded + alphabet[value]
    print(f"Here is your {en_or_de}d message {decoded}")


def cipher(message, shift_number, en_or_de):
    if en_or_de == "encode":
        encrypt(message, shift_number)
    else:
        decrypt(message, shift_number)


cipher(message, shift_number, en_or_de)
