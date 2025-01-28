## Adit Gautam
# 1/27/25
# Chapter 3 Lab 1 Task 2
# A program to calculate the shipping cost 

response = input("Are you shipping internationally (yes or no)?")
response = response.lower()                                         #Avoids user error if they type in caps

if response != "yes" :                                              #If no, jump straight t o else
    response = input("Are you shipping continental (yes or no)?")
    response = response.lower()
    if response != "yes" :                                          #I COULD HAVE MADE THIS BLOCK A LOT MORE CLEAN
        print("The shipping rate is $10.00")                        #I USUALLY DO NOT WRITE CODE LIKE THIS BUT ITS LATE
    else :
        print("The shipping rate is $5.00")
else : 
    print ("The shipping rate is $10.00")

