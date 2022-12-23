#!/usr/bin/env python3
import random
import os
import hangman_art
import hangman_words


chosen_word = list(random.choice(hangman_words.word_list))
lives = 6

answer = []
for i in range(len(chosen_word)):
    answer += "_"

end_of_game = False

print(hangman_art.logo)
print(f"Pssst, the solution is {''.join(chosen_word)}.")

while not end_of_game:
    user_guess = input("Gues a latter from the world: ").lower()
    
    os.system("clear")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == user_guess:
            if answer[i] != letter:
                answer[i] = letter
            else:
                print(f"The {letter} is already guessed")

    if user_guess not in chosen_word:
        print("Wrong letter - one life lost.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    
    print(hangman_art.stages[lives])
    print(f"{''.join(answer)}")

    if "_" not in answer:
        end_of_game = True
        print("You win!")
    

