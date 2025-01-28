#Adit Gautam
#CS003C Project 1
#1/27/25

from math import ceil                                                       #Need for rounding paint gallons

##########################################################################
# Function: round_dollar                                                 #                                  
# Arguments: integer or double amount to round                           #
# Example arguments include: "7.27", "0.00", "5", "0.52"                 #
# Purpose: Properly rounds doubles to an integer dollar and cents amount #
# Only rounds last 2 digits                                              #
##########################################################################


def round_dollar(amount) :                                                  #Helper function to properly round dollars\
    str_amount = str(amount)                                                #Convert float or int to string
    if '.' in str_amount :                                                  #Check if there is a decimal value                                                 
        dollars, cents = str_amount.split('.')                              #Split the string into before and after the decimal
    else :
        dollars = str_amount                                                #If there is no cents value
        cents = "00"                                                        #So that integer dollar values round properly
    if cents != "00" :
        cents = (cents)[:3]                                                 #If cents have a value, find the first 3 digits so we can round
        cents_value = int(cents) * 0.1                                      #Multiply by .1 so we can use math.ceil()
        cents_value = ceil(cents_value)
        cents = str(cents_value).zfill(2)
    final_result = dollars + '.' + cents                                    #Concatenate the strings and reintroduce decimal
    return final_result

    
    
gallon_coverage = 350                                                       #Const, but we can make it modular
sales_tax = .07

#Step 1: Read inputs

wall_height = float(input("Enter the wall height:"))
wall_width = float(input("Enter the wall width:"))
cost_per_gallon = float(input("Enter the paint cost per gallon ($):"))

#Calculate and print the wall area

wall_area = wall_height * wall_width
print("Wall area:", f"{wall_area:.1f}", "sq ft" )                           #Format specifier for one decimal place

#Step 2: Calculate and output amount of paint

number_of_gallons = wall_area / gallon_coverage
print("Paint needed ", f"{number_of_gallons:.3f}", "gallons")

#Step 3: output the number of 1 gallon cans (as integer)
cans_needed = ceil(number_of_gallons)                                       #Store for later use, need as an int
print("Cans needed:", cans_needed, "can(s)")

#Step 4: Calculate and output the paint cost
paint_cost =  cans_needed * cost_per_gallon
print("Paint cost: $" + round_dollar(paint_cost))

tax = sales_tax * paint_cost                                                #Can use the const value, or input for modularity
print("Sales tax: $" + round_dollar(tax))

total_cost = paint_cost + tax
print("Total cost: $" + round_dollar(total_cost))                           #Use the round dollar function to round each time