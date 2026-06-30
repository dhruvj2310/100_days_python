intro = """
 _       __     __                             __
| |     / /__  / /________  ____ ___  ___     / /_____
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/

     █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
    ███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
    ██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
    ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

print(intro, "\n\nWelcome to secret auction program.")

all_bids = {}

stop = False

while not stop:
    name = input("\nWhat is your name?: ")
    bid = int(input("What is your bid?: "))

    all_bids[name] = bid

    conti = input("\nAre there any more bidders? 'yes' or 'no': ")

    if conti == "no":
        stop = True
    else:
        print("\n" * 200)

highest_bid = 0
winner = ""

for bidder in all_bids:
    if all_bids[bidder] > highest_bid:
        highest_bid = all_bids[highest_bid]
        winner = bidder

print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")