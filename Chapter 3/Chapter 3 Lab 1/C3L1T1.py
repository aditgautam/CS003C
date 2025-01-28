## Adit Gautam
# 1/27/25
# Chapter 3 Lab 1 Task 1
# A program to calculate a discount based on 

from math import ceil 

def round_dollar(amount) :                                                  #Helper function to properly round dollars\
    str_amount = str(amount)                                                #Convert float or int to string
    if '.' in str_amount :                                                  #Check if there is a decimal value                                                 
        dollars, cents = str_amount.split('.')                              #Split the string into before and after the decimal
    else :
        dollars = str_amount                                                #If there is no cents value
        cents = "00"                                                        #So that integer dollar values round properly
    if len(cents) < 2 :                                                     #For example, if there are 1 or 0 digits in cents
        cents = cents.ljust(2, '0')                                         #Adjusts length to 2. Fills anything mjissing with 0 
    elif len(cents) > 2 :                                                   #If theres  more than 2, then we go through with rounding
        cents  = str(ceil(int(cents[:3]) * 0.1)).zfill(2)
    #IF CENTS IS EXACTLY 2, THEN DO NOT DO ANYTHING
    return dollars + '.' + cents                                         

def discount(purchase_price) :
    print("The purchase price is: $" + round_dollar(purchase_price))
    if purchase_price < 128 :                                               #Set discount initialization based on purchase price
        discount = .08
    else : 
        discount = .16
    discount_value = purchase_price * discount                              #Find dollar amount
    # print("Discount value:",discount_value)                                 #DEBUG
    discounted_price = purchase_price - discount_value    
    # print("Discounted price:", discounted_price)                            #DEBUG       

    print("The price after the discount $" + round_dollar(discounted_price))

def discount_input() : 
    purchase_price =  input("Please enter the total purchase price:")
    discount(purchase_price)                                                #Print should get called                                                    

def main() : 
    print("Test 1: Price = 245")
    discount(245)
    print()
    print("Test 2: Price = 100")
    discount(100)
    print()
    print("Edge case: Price == 128")
    discount(128)

main()
    