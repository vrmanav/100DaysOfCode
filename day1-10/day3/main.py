# Day 3 - Treasure Island 

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? [LEFT/RIGHT]\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. [SWIM/WAIT]\n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
        print("+────────────────────────────────────────+")
        print(f"│It's a room full of fire 🔥 Game Over 💀│")
        print("+────────────────────────────────────────+")
    elif choice3 == "yellow":
        print("+───────────────────────────+")
        print(f"│CONGRATULATIONS YOU WIN 🎉 │")
        print("+───────────────────────────+")
    elif choice3 == "blue":
        print("+──────────────────────────────────────────+")
        print(f"│You enter a room of beasts 👹 Game Over 💀│")
        print("+──────────────────────────────────────────+")
    else:
        print("+─────────────────────────────────────────────────+")
        print(f"│You chose a door that doesn't exist. Game Over 💀│")
        print("+─────────────────────────────────────────────────+")
  else:
    print("+──────────────────────────────────────────────────+")
    print(f"│You get attacked by an angry trout 🐟 Game Over 💀│")
    print("+──────────────────────────────────────────────────+")
else:
    print("+────────────────────────────────────+")
    print(f"│You fell into a hole 🕳️  Game Over 💀│")
    print("+────────────────────────────────────+")
