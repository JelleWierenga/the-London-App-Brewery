MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0


quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

while True:
    choice = input("What would you like? (espresso, latte, cappuccino): ").lower()

    if choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value} ml/g")

    if choice == "latte":
        if (
            MENU["latte"]["ingredients"]["water"] <= resources["water"]
            and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]
            and MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]
        ):
            print("Please insert coins")
            input_quarters = int(input("How many quarters: "))
            input_dimes = int(input("How many dimes: "))
            input_nickels = int(input("How many nickels: "))
            input_pennies = int(input("How many pennies: "))
            price = MENU["latte"]["cost"]
            print(f"A latte costs ${price}")
            inserted = (input_quarters * quarter) + (input_pennies * penny) + (input_nickels * nickle) + (input_dimes * dime)

            if inserted >= price:
                change = round(inserted - price, 2)
                print(f"Here is your change: ${change}")
                money_in_machine += price

                water = MENU["latte"]["ingredients"]["water"]
                milk = MENU["latte"]["ingredients"]["milk"]
                coffee = MENU["latte"]["ingredients"]["coffee"]

                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee

                for key, value in resources.items():
                    print(f"{key}: {value} ml/g")
            else:
                print(f"You inserted ${inserted}, but you need to pay ${price}. Please insert more coins.")
        else:
            print("Sorry, not enough ingredients for a latte. Program stopped.")
            break

    if choice == "espresso":
        if (
            MENU["espresso"]["ingredients"]["water"] <= resources["water"]
            and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]
        ):
            print("Please insert coins")
            input_quarters = int(input("How many quarters: "))
            input_dimes = int(input("How many dimes: "))
            input_nickels = int(input("How many nickels: "))
            input_pennies = int(input("How many pennies: "))
            price = MENU["espresso"]["cost"]
            print(f"An espresso costs ${price}")
            inserted = (input_quarters * quarter) + (input_pennies * penny) + (input_nickels * nickle) + (input_dimes * dime)

            if inserted >= price:
                change = round(inserted - price, 2)
                print(f"Here is your change: ${change}")
                money_in_machine += price

                water = MENU["espresso"]["ingredients"]["water"]
                coffee = MENU["espresso"]["ingredients"]["coffee"]

                resources["water"] -= water
                resources["coffee"] -= coffee

                for key, value in resources.items():
                    print(f"{key}: {value} ml/g")
            else:
                print(f"You inserted ${inserted}, but you need to pay ${price}. Please insert more coins.")
        else:
            print("Sorry, not enough ingredients for an espresso. Program stopped.")
            break

    if choice == "cappuccino":
        if (
            MENU["cappuccino"]["ingredients"]["water"] <= resources["water"]
            and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]
            and MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]
        ):
            print("Please insert coins")
            input_quarters = int(input("How many quarters: "))
            input_dimes = int(input("How many dimes: "))
            input_nickels = int(input("How many nickels: "))
            input_pennies = int(input("How many pennies: "))
            price = MENU["cappuccino"]["cost"]
            print(f"A cappuccino costs ${price}")
            inserted = (input_quarters * quarter) + (input_pennies * penny) + (input_nickels * nickle) + (input_dimes * dime)

            if inserted >= price:
                change = round(inserted - price, 2)
                print(f"Here is your change: ${change}")
                money_in_machine += price

                water = MENU["cappuccino"]["ingredients"]["water"]
                milk = MENU["cappuccino"]["ingredients"]["milk"]
                coffee = MENU["cappuccino"]["ingredients"]["coffee"]

                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee

                for key, value in resources.items():
                    print(f"{key}: {value} ml/g")
            else:
                print(f"You inserted ${inserted}, but you need to pay ${price}. Please insert more coins.")
        else:
            print("Sorry, not enough ingredients for a cappuccino. Program stopped.")
            break

    if choice == "exit":
        break
