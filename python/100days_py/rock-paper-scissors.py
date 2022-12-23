#!/usr/bin/env python3
import random

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

game_images = [rock, paper, scissors]


#Let the player to make their choise

choise = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choise >= 3 or choise < 0:
    print('You lose!')
else:
    print(game_images[choise])

    #PC choise related to the random module

    print("Computer choise:")

    pc_choise = random.randint(0,2)
    print(game_images[pc_choise])
    
    #Let`s find out who win
    
    result = [choise, pc_choise]
    
    win = [[0, 2], [2, 1], [1, 0]]
    lose = [[2, 0], [1, 2], [0, 1]]
    
    if result in win:
        print("You win!")
    elif result in lose:
        print("You lose...")
    else:
        print("It`s a draw")
