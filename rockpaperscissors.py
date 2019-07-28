print(
"""            
                _      
               | |                                            (_)
 _ __ ___   ___| | __   _ __   __ _ _ __   ___ _ __   ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ /  | '_ \ / _` | '_ \ / _ \ '__| / __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <   | |_) | (_| | |_) |  __/ |    \__ \ (__| \__ \__ \ (_) | |  \__ /
|_|  \___/ \___|_|\_\, | .__/ \__,_| .__/ \___|_|,   |___/\___|_|___/___/\___/|_|  |___/.
                       | |         | |
                       |_|         |_|
""")

rock = (
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Compared to the code given in the notebook, this while loop will make sure the input definitely matches an option.
while True:
    player_input = input("What do you choose? ")
    choice = player_input.lower()
    if choice == "rock":
        print(rock)
        break
    if choice == "paper":
        print(paper)
        break
    if choice == "scissors":
        print(scissors)
        break
        
import random

computer_choice = random.randint(1,3)

if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
else:
    print(scissors)

if (choice == "rock") and (computer_choice == 1):
    print("IT'S A DRAW!")
elif (choice == "paper") and (computer_choice == 2):
    print("IT'S A DRAW!")
elif (choice == "scissors") and (computer_choice == 3):
    print("IT'S A DRAW!")
elif (choice == "rock") and (computer_choice == 3):
    print("YOU WIN!")
elif (choice == "rock") and (computer_choice == 2):
    print("YOU LOSE!")
elif (choice == "paper") and (computer_choice == 1):
    print("YOU WIN!")
elif (choice == "paper") and (computer_choice == 3):
    print("YOU LOSE!")
elif (choice == "scissors") and (computer_choice == 2):
    print("YOU WIN!")
else:
    print("YOU LOSE!")
print("\n")

print("Thank you for playing!")
print("\n")
input("Press ENTER to exit")
