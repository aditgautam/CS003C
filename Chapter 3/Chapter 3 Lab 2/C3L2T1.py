## Adit Gautam
# 1/28/25
# Chapter 3 Lab 2 Task 1
# A program that tells us if all the integers are the same

# I really want to make this modular using some data structures and sort methods but it will take too  long

#input 
int1 = input("Enter the first integer:")
int2 = input("Enter the second integer:")
int3 = input("Enter the third integer:")

#compare
if int1 == int2 == int3 :                   #Just immediately check for equality of all 3
    print("They are all the same.")                   #No need for nested ifs
elif int1 != int2 and int1!= int3 and int2!= int3 : #Check that each value is not the same as the other TWO\
    print("They are all different.")
else :                                      #If the other 2 conditions are not satisfied this is all that is left
    print("Thay are neither the same or different")