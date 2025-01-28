## Adit Gautam
# 1/28/25
# Chapter 4 Lab 1 Task 1
# Program to find sum of digits

sum = 0                         #Not sure if initialization is required in python
i = 0                           #Counter since no i++

number = input("Enter a positive number:")

while i < len(number) :
    current = int(number[i])    #grab the current digit
    sum += current              #add to the sum
    i+=1                        #i++

print("The sum of the digits is:", sum)



