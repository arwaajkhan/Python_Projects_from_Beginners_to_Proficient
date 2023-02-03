rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#code below

import random
l1 = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice > 2 or user_choice < 0:
  print("Entered invalid number, You lose")
else:
  print(l1[user_choice])
  comp_choice = random.randint(0,2)
  print("Computer chose")
  print(l1[comp_choice])
  if(user_choice == comp_choice):
    print("It's a draw")
  elif((user_choice == 0 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1) or (user_choice == 1 and comp_choice == 0)):
    print("You win")
  else:
    print("You lose")
    