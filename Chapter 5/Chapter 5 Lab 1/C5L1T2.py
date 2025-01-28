## Adit Gautam
# 1/28/25
# Chapter 5 Lab 1 Task 2
# Function to evaluate arithmetic

def evaluates(operator, a, b) :
    match operator:
        case "+" :
            return a + b
        case "-" : 
            return a - b
        case "*" :
            return a * b
        case "/" :
            assert b!= 0, "Cannot divide by 0"  #Slight error handling not very clear
            return a / b
        case "**" :
            return a ** b
        case _ :
            print("Invalid operator")           #Should i pass here or return
            return                              #Empty return?
        

def main() :
    operator = input("Enter operator (+, -, *, /, **):")
    a = int(input("Enter the first integer:"))
    b = int(input("Enter the second integer:"))
    print(f"{evaluates(operator, a, b):.2f}")

main()