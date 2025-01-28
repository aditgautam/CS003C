## Adit Gautam
# 1/27/25
# Chapter 2 Lab 3 Task 2
# A program that swaps the middle 2 characters in an even length string

def swap_middle(string) :                       #Make it a function to test 3 times
    assert len(string) >= 4                     #Lab guidelines
    if len(string) % 2 != 0 :                   #If string length is not even, swapping the middle returns original string
        return string
    else :
        length = len(string)                    #Get string length                              
        position1 = (length //  2)               #For example, 6 / 2 yields index 3. We would want to swap index 2 and 3  
        position2 = (position1 - 1)             # 0 1 2 3 4 5, notice how the middle two are 2 and 3. Go -1 to find position 2

        # temp = string[position2]                #Array arithmetic
        # string[position2] = string[position1]
        # string[position1] = temp

        
        #RUNNING INTO A HUGE ERROR HERE, FORGOT STRINGS ARE IMMUTABLE

        #create new string

        swapped = (string[:position2] + string[position1] + string[position2] + string[(position1 + 1):])
        #NEWSTRING = everything before pos2 + SWAP + SWAP + everything after the sawp

        return swapped                          #Return the swapped string
    
def print_transformation(string, swapped) :
    print(string, "->", swapped)
    
def main() : 
    print_transformation("Java", swap_middle("Java"))
    print_transformation("123456", swap_middle("123456"))
    print_transformation("Computer", swap_middle("Computer"))
main()
