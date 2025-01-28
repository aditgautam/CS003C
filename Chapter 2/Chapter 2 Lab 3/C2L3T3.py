## Adit Gautam
# 1/27/25
# Chapter 2 Lab 3 Task 2
# A program that swaps the middle 2 characters in an even length string
from math import ceil 

#USING AN OLD FUNCTION FROM PROJECT 1

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

def find_total_cost(car_cost, mperyear, gas_price, mpg, resale, years) :    #Just make it a function to make life easier
    print("Total cost of the car:", car_cost)
    print("How many miles will you drive each year?", mperyear)
    print("Price of gas per gallon:", gas_price)
    print("Fuel efficiency in mpg:", mpg)
    print("You can sell the car for:", resale)

    total_cost = car_cost + ((mperyear/mpg) * years * gas_price) - resale    #Basic algorithm + initial cost + operating cost - resale

    print("The total cost of ownership is $" + round_dollar(total_cost) )

def main() :
    find_total_cost(40000, 15000, 4, 50, 18000, 5)                           #Just enter all the parameters at once  
    print()                                                                  #std::endl
    find_total_cost(24000, 15000, 4, 50, 8000, 5)

main()