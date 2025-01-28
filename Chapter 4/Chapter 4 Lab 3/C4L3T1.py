## Adit Gautam
# 1/28/25
# Chapter 4 Lab 3 Task 1
# Random Number Generator

from random import randint

for i in range(1,6) :
    roll1 = randint(1,6)    #Random integer between 1 and 6, inclusive
    roll2 = randint(1,6)
    sum = roll1 + roll2
    print(f"Roll {i}: Dice 1 = {roll1}, Dice 2 = {roll2}, Total = {sum}")   #remember to add "f" before the string


