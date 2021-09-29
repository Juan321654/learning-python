from art import logo
print(logo)

bidders = {}
# {"Juan": 50, "Steph": 60}

is_bidding_done = False

while not is_bidding_done:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid # "name": money

    def clearConsole(): return print('\n' * 150)
    done = input("Are there any other bidders? Type 'yes' or 'no'.: ").lower()

    highest_bid = 0
    winner = ""

    if done == 'no':
        for bidder in bidders:
            bid_amount = bidders[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winnder is {winner} with ${highest_bid}")
        is_bidding_done = True
    if done == 'yes':
        clearConsole()
