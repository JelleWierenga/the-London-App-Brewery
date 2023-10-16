print("Welcome to the tip calculator.")
total_bill: float = float(input("What was the total bill? "))
tip_percentage: int = int(input("What perentage tip would you like to give? 10, 12 or 15? "))
people_count: int = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
total_plus_tip = total_bill + tip_amount
split_bill = total_plus_tip / people_count
print(f"Each person should pay: ${split_bill}")
