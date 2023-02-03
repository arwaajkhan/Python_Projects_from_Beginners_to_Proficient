from replit import clear
from art import logo

print(logo)

bid_dict = {}
choice = True
winner = ''
while choice:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    user_choice = input("Are there any other bidders? type 'yes' or 'no'. \n")
    if user_choice == 'yes':
        clear()
    else:
        value = 0
        for key in bid_dict:
            if value < bid_dict[key]:
                value = bid_dict[key]
                winner = key
        choice = False
clear()
print(f"The winner is {winner} with a bid of ${value}")
