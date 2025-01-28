## Adit Gautam
# 1/28/25
# Chapter 3 Lab 3 Task 2
# Identify the contents of a string given methods


#Im way too used to C++ 14. Python is so easy?
#I was about to build a full string parser

str = input("Enter any string:")

if str.isalpha() : 
    print("all letters")
elif str.isdigit() : 
    print("all digits")
elif str.isalnum() :
    print("letters and digits")
else : 
    print("mix of all")