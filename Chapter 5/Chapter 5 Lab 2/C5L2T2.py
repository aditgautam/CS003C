## Adit Gautam
# 1/28/25
# Chapter 5 Lab 2 Task 2
# Greeting function

def sup(name, greeting = "Hello") :
    if greeting.strip() == "" :             #I COULDN'T FIND THE PROPER WAY TO DO THIS HELP>
        greeting = "Hello"                  #Should this not already happen?

    greeting = greeting.lower()                        #All lowercase
    greeting = greeting.capitalize()                   #Capitalizes first letter
    print(greeting + ',' , name + "!")

def main() : 
    name = input("Enter your name: ")
    greeting = input("Enter a greeting or press enter: ")
    sup(name, greeting)

main()

