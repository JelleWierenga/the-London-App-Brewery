import random
import Words

lives = 6
chosen_word = random.choice(Words.word_list).lower()

display = ["_" for i in chosen_word]
print(display)
while "_" in display and lives > 0:
    guess = input("Letter: ").lower()
    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives = lives - 1
        print(f"You have {lives} left")
    print(" ".join(display))

print(f"Congratulations! You guessed the word: {chosen_word} and with {lives} to spare")
