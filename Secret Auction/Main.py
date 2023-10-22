print("Welcome to the secret auction program")

bids = {}
max_bidder = None
max_bid = 0

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid: $"))

    bids[name] = bid

    other_person = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_person != "yes":
        break

for name, bid in bids.items():
    if bid > max_bid:
        max_bid = bid
        max_bidder = name

if max_bidder:
    print(f"The person with the highest bid is '{max_bidder}' with a bid of ${max_bid}")
else:
    print("The dictionary is empty.")
