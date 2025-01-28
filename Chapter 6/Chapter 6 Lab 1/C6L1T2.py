## Adit Gautam
# 1/28/25
# Chapter 6 Lab 1 Task 2
# Alternating Sums

adding = True                   #This is how we will track our alternation
user_number = 0                 #Poor man's do while loop
sum = 0                         #Start the counter

while user_number != "Q" :
    user_number = input("Enter Values (blank line to quit): ")
    if user_number == "Q" :      #If this is a blank then just quit out
        break
    if adding : 
        sum += int(user_number) #We need to conver this to an int
        adding = not adding     #When it is stored as a string we cannot use arithmetic
    else :                      #If we convert too early we can't have a break casee
        sum -= int(user_number)
        adding = not adding

print(f"The alternating sum is {sum:.1f}")
