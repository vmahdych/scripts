#!/usr/bin/env python3

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(len(names))

winner = names[random.randint(0, (len(names)-1))]

print(f"{winner} is going to buy the meal today!")
