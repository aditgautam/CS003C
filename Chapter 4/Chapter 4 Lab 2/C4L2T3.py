## Adit Gautam
# 1/28/25
# Chapter 4 Lab 2 Task 3
# Count the number of vowels in a string

str = input("Enter a string:")

index = 0
vowels = 0

while index < len(str) : 
    current = str[index].lower()
    # print(current)

    match current :
        case 'a' | 'e' | 'i' | 'o' | 'u' :  #Its | and not , or ||
            vowels +=1
        case _ :                            # _ is default
            pass                            # I think this is python break;
    index +=1

if vowels == 0  : 
    print("The string has no vowels")
elif vowels == 1 :
    print("The string has 1 vowel")
else :
    print("The string has", vowels, "vowels")