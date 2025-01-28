## Adit Gautam
# 1/28/25
# Chapter 5 Lab 2 Task 2
# Integer information

#Calculates and returns the number of digits in the number
def digits(num) :
    return len(str(num))                                        #Return the length as an int so we can call it

#Returns the first digit in the number
def firstDigit(num) :
    return int(str(num[0]))                                     #Zero index

#Returns the last digit in the  number
def lastDigit(num) :
    return int(str(num[digits(num) - 1]))                       #length - 1  for array arithmetic

#Prints all the information for the number (VOID)
def printing(num) :
    print(f"The number of digits in {num} is", digits(num))
    print(f"The first digit in {num} is", firstDigit(num))
    print(f"The first digit in {num} is", lastDigit(num))

def main() :
    user_input = input("Enter any positive integer: ")
    printing(user_input)

main()