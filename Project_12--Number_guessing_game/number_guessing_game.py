
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 101)


#Calculation part
def calculating(n, l_n):
    for i in range(l_n, 0, -1):
        print(f"You have {i} attempts remaning to guess the number")
        user_input = int(input("Make a guess: "))
        if user_input < n:
            print("Too low")
            print("Guess again")
        elif user_input > n:
            print("Too high")
            print("Guess again")
        else:
            print(f"You got it! The answer was {n}.")
            break


#choosing level
if choice == 'easy':
    calculating(number, 10)
elif choice == 'hard':
    calculating(number, 5)
else:
    print("Please enter a valid level")
