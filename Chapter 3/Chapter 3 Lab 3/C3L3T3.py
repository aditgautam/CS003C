## Adit Gautam
# 1/28/25
# Chapter 3 Lab 3 Task 3
# Program to find the number of days given a month

month = int(input("Enter your month as a number:"))

match month:                                        #BASICALLY A SWITCH CASE. WHATS THE DIFFERENCE?
    case 1 | 3 | 5 | 7 | 8 | 10 | 12  :
        print("There are 31 days")
    case 4 | 6 | 9 | 11 :                           #30 day months
        print("There are 30 days")
    case 2 : 
        print("There are 28 or 29 days")
    case default :                                  #Was going to create a do while loop for invalid input
        print("Invalid month")