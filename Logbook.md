# Day 1

Today, I completed the first challenge of The London App Brewery's 100 Days of Code Challenge. It was all about using input and combining strings into one and then printing them out. For this task, I created a Band Name Generator that takes two inputs: the name of the city you were born in and the name of your pet. It then combines these two inputs to create a unique band name.

For example, if the city is "Miami" and the pet's name is "Bunny," the generated band name would be "Miami Bunny."

Here's a code sample to illustrate how I used the `input()` function to collect user data in Python:

```python
city = input("Enter the name of the city you were born in: ")
pet_name = input("Enter the name of your pet: ")

# Combine the inputs to create a band name
band_name = city + " " + pet_name

# Print the generated band name
print(f"Your band name is: {band_name}")
```
You can check out the code I used for Day 1 on [GitHub: Band name generator](https://github.com/JelleWierenga/the-London-App-Brewery/tree/main/Band%20name%20generator).


This code sample demonstrates how to use the `input()` function to collect user input and then combine the provided values to generate a band name.


---
# Day 2

Today, I continued my coding journey with The London App Brewery's 100 Days of Code Challenge. I worked on a Tip Calculator, which is a handy tool to quickly calculate how much each person should pay when splitting a bill at a restaurant.

Here's the Python code I used for the Tip Calculator:

```python
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
total_plus_tip = total_bill + tip_amount
split_bill = total_plus_tip / people_count

print(f"Each person should pay: ${split_bill:.2f}")
```
You can check out the code I used for Day 2 on [GitHub: Tip calculator](https://github.com/JelleWierenga/the-London-App-Brewery/tree/main/Tip%20Calculator).

---
# Day 3

Today, I continued my journey with The London App Brewery's 100 Days of Code Challenge, and it was an adventurous day working on the "Treasure Island" project.

You can check out the code I used for Day 3 on [GitHub: Treasure island](https://github.com/JelleWierenga/the-London-App-Brewery/tree/main/Treasure%20island).

This project is an exciting text-based adventure game where the player's choices determine the outcome. I had to make decisions at crossroads, explore lakes, and face dark forests. It's not just about coding; it's about creating interactive experiences. Looking forward to what the next days will bring!

---
# Day 4
Today i did day 4 of this challange. i made a Rock Paper Sissors game using if elif and else statments

Check out what i made today here [Github: Rock Paper Sissors](https://github.com/JelleWierenga/the-London-App-Brewery/tree/main/Rock%20Paper%20Sissors)

---
# Day 5
It is day 5 already and i am feeling great. today was all about while loops and for loops.

The challange was to make a password generator that generates a password with random characterss form a list.

Do you want to generate strong passwords?(ofcourse you do) check it out here [Github: Password generator](https://github.com/JelleWierenga/the-London-App-Brewery/tree/main/Password%20generator)

---
# Day 6
I have not much to say today. i learned about functions and did some training online. it was fun :)

---
# Day 7
Today i made a hangman game. that was tough to do, this was the first real challange i got and i liked it
I had to use everything i learned so far for this project. and i had to use 2 files for this, i like that. i have 1000 random words in the Words.py file and i did not need that in the main file so a second file it is.

I bet you want to play the game now :). Dont worry you can find it here [Guthub: Hangman](https://github.com/JelleWierenga/the-London-App-Brewery/tree/main/Hangman)
