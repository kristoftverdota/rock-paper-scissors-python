import art
import random

computer = random.randint(0, 2)
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player == 0:
  print(rock)
  if computer == 0:
    print(f"Computer chose:\n{rock}")
    print("Draw")
  elif computer == 1:
    print(f"Computer chose:\n{paper}")
    print("You lose")
  elif computer == 2:
    print(f"Computer chose:\n{scissors}")
    print("You win")
    
elif player == 1:
  print(paper)
  if computer == 0:
    print(f"Computer chose:\n{rock}")
    print("You win")
  elif computer == 1:
    print(f"Computer chose:\n{paper}")
    print("Draw")
  elif computer == 2:
    print(f"Computer chose:\n{scissors}")
    print("You lose")
    
elif player == 2:
  print(scissors)
  if computer == 0:
    print(f"Computer chose:\n{rock}")
    print("You lose")
  elif computer == 1:
    print(f"Computer chose:\n{paper}")
    print("You win")
  elif computer == 2:
    print(f"Computer chose:\n{scissors}")
    print("Draw")
