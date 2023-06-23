# Day 4 - ROCK-PAPER-SCISSORS

from art import rock, paper, scissors
from random import randint
def show_menu():
    print("1: ROCK")
    print("2: PAPER")
    print("3: SCISSORS")

symbols = [rock, paper, scissors]
print("What do you choose?")
show_menu()
user_choice = int(input())-1
print(symbols[user_choice])
comp_choice = randint(0, 2)
print(f"Computer chose {symbols[comp_choice]}")
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose 🙁") 
elif user_choice == 0 and comp_choice == 2:
  print("You win! 🎉")
elif comp_choice == 0 and user_choice == 2:
  print("You lose 🙁")
elif comp_choice > user_choice:
  print("You lose 🙁")
elif user_choice > comp_choice:
  print("You win! 🎉")
elif comp_choice == user_choice:
  print("It's a draw ⛔️")