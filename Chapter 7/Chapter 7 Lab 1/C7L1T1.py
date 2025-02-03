## Adit Gautam
# 2/2/25
# Chapter 7 Lab 1 Task 1
# File Average

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

lines = [line.strip() for line in infile]       # Easily split the lines

numbers = []                                    # New empty list that we will append into 

for line in lines : 
    number = int(line)                          # Convert str to int so we can use summation
    numbers.append(number)

total = sum(numbers)
average = total / (len(numbers))

for number in numbers : 
    outfile.write(f"{number}\n")                # use fstream for formatting
    print(number)
outfile.write(f"Total = {total}\n")
print(f"Total = {total}\n")
outfile.write(f"Average = {average}\n")
print(f"Average = {average}\n")

infile.close()
outfile.close()



