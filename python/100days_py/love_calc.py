#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
l_c_names = lower_case_name1 + lower_case_name2

true_count = 0
love_count = 0

for i in list("true"):
    true_count += l_c_names.count(i)

#print(true_count)

for i in list("love"):
    love_count += l_c_names.count(i)
   
#print(str(true_count) + str(love_count))

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

