## Adit Gautam
# 1/27/25
# Chapter 2 Lab 2 Task 3
# A program that performs some basic string operations

str = "Java1"                                           #Can take an input

print("The string is", str)
print("*-*-*-*-*-*-*-*-*-*-*")                          #Hardcoded

length = len(str)
print("The length of the string is", length)

temp_str = str                                          #Dont override contents  of original string
temp_str.replace('a', 'A')
print("The replaced string is", temp_str)

temp_str = str.upper()
print("The captialized string is", temp_str)

if length > 1 :                                         #Cant find the second character if string is empty or 1 char
    print("The second character is", str[1])
else :
    print("String length too short to find the second character")

assert length > 0, "String was empty or had an error"   #Making sure we don't have an empty string

print("The last character is", str[length - 1])
print("The middle character is", str[(length // 2)])



