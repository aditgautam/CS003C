## Adit Gautam
# 1/27/25
# Chapter 2 Lab 2 Task 2
# A program to direct a cashier on how to give change

due = 323
received = 693

print("Due:" , due, "Received:", received)

change = received - due                     #Find amount of pennies change

assert change >= 0                          #Break if invalid amoujnt

print("The change is:")

dollars = change // 100                     #Floor division by  
print(dollars, "dollars")                   #Print 
change = change % 100                       #Update change with the remaining amount  

quarters = change // 25
print(quarters, "quarters")
change = change % 25

dimes = change // 10 
print(dimes, "dimes")
change = change % 10

nickels = change // 5
print(nickels, "nickels")
change = change % 5

pennies = change
print(pennies, "pennies")
