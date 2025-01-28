## Adit Gautam
# 1/28/25
# Chapter 4 Lab 2 Task 4
# Count the number of vowels in a string

#initialize counters
char_counter = 0
digit_counter = 0
symbol_counter = 0

str = input("Enter a string:")

for ch in str :                                 #For each index in the character array
    if ch.isalpha() :
        char_counter +=1
    elif ch.isdigit() :
         digit_counter +=1
    else :
        symbol_counter +=1

print("Total counts of Chars =", char_counter)
print("Total counts of digits =", digit_counter)
print("Total counts of Symbol =", symbol_counter)    