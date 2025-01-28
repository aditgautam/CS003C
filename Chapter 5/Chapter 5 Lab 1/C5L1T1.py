## Adit Gautam
# 1/28/25
# Chapter 5 Lab 1 Task 1
# Function to find sum

def find_sum(n) :
    #initialize counter
    sum = 0

    for i in range(n+1) :       #We want to include n in what we add
        sum +=  i
    return sum                  #Return once we break the  loop

def main() :
    user_input = int(input("Enter an integer:"))
    print("The result is", find_sum(user_input))

main()