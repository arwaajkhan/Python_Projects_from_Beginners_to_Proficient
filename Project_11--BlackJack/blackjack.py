#BLACK-JACK

import random
from art import logo
from replit import clear

play_game = True
while play_game:
    option = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if option == 'y':
        clear()
        print(logo)
        user_list = []
        comp_list = []
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for i in range(2):
            user_list.append(random.choice(cards))
            comp_list.append(random.choice(cards))
        print(f"Your cards: {user_list}, current score: {sum(user_list)}")
        print(f"Computer's first card: {comp_list[0]}")

        #Both card either of us got Ace
        if user_list[0] == user_list[1] == 11:
            user_list[1] = 1
            print("You got two Ace hence one is modified")
            print(f"Your cards: {user_list}, current score: {sum(user_list)}")
        if comp_list[0] == comp_list[1] == 11:
            comp_list[1] = 1
            print("Dealer got two Ace hence one is modified")
            print(f"Computer's first card: {comp_list[0]}")

# BlackJack Testing
        value = 'Pass'
        if sum(comp_list) == sum(user_list) == 21:
            print(f"Your cards: {user_list}, total score: {sum(user_list)}")
            print(f"Dealer cards: {comp_list}, total score: {sum(comp_list)}")
            print("Both got BlackJack it's Draw")
            value = 'Fail'
        elif sum(user_list) == 21:
            print(f"Your cards: {user_list}, total score: {sum(user_list)}")
            print(f"Dealer cards: {comp_list}, total score: {sum(comp_list)}")
            print("Congrats you got the BlackJack, You win")
            value = 'Fail'
        elif sum(comp_list) == 21:
            print(f"Your cards: {user_list}, total score: {sum(user_list)}")
            print(f"Dealer cards: {comp_list}, total score: {sum(comp_list)}")
            print("Dealer got the BlackJack, \n You lose ")
            value = 'Fail'

#operation and calculation
        elif value == 'Pass':
            user_choice = True
            while user_choice:
                choice = input(
                    "Type 'y' to get another card, type 'n' to pass: ")

                #User-choice is yes
                if choice == 'y':
                    user_list.append(random.choice(cards))
                    print(
                        f"Your cards: {user_list}, current score: {sum(user_list)}"
                    )
                    print(f"Computer's first card: {comp_list[0]}")
                    if sum(user_list) < 22:
                        continue
                    elif 11 in user_list:
                        user_list[user_list.index(11)] = 1
                        print(
                            f"Yours new list after replacing Ace {user_list}, current total {sum(user_list)}"
                        )
                        if sum(user_list) > 21:
                            print(
                                f"Your cards: {user_list}, final score: {sum(user_list)}"
                            )
                            print(
                                f"Dealerr cards: {comp_list}, final score: {sum(comp_list)}"
                            )
                            print("Burst: You lose")
                            user_choice = False
                    else:
                        print(
                            f"Your cards: {user_list}, final score: {sum(user_list)}"
                        )
                        print(
                            f"Dealerr cards: {comp_list}, final score: {sum(comp_list)}"
                        )
                        print("Burst: You lose")
                        user_choice = False

#choice is no
                else:
                    comp_choice = True
                    while comp_choice:
                        if sum(comp_list) < 22:
                            if (sum(comp_list) >
                                    sum(user_list)) and sum(comp_list) > 16:
                                print(
                                    f"Your cards: {user_list}, final score: {sum(user_list)}"
                                )
                                print(
                                    f"Dealer cards: {comp_list}, final score: {sum(comp_list)}"
                                )
                                print("You lost")
                                comp_choice = user_choice = False
                            elif (sum(comp_list)
                                  == sum(user_list)) and sum(comp_list) > 16:
                                print(
                                    f"Your cards: {user_list}, final score: {sum(user_list)}"
                                )
                                print(
                                    f"Dealerr cards: {comp_list}, final score: {sum(comp_list)}"
                                )
                                print("It's a draw")
                                comp_choice = user_choice = False
                            elif (sum(comp_list)
                                  == sum(user_list)) and sum(comp_list) < 17:
                                comp_list.append(random.choice(cards))
                            elif sum(comp_list) < sum(user_list):
                                comp_list.append(random.choice(cards))
                        else:
                            if 11 in comp_list:
                                comp_list[comp_list.index(11)] = 1
                            else:
                                print(
                                    f"Your cards: {user_list}, final score: {sum(user_list)}"
                                )
                                print(
                                    f"Dealerr cards: {comp_list}, final score: {sum(comp_list)}"
                                )
                                print("Dealer Burst: You win")
                                comp_choice = user_choice = False
            user_choice = False
# Don't wanna play the game
    else:
        play_game = False
