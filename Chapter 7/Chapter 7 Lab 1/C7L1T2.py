## Adit Gautam
# 2/2/25
# Chapter 7 Lab 1 Task 1
# Column File Average

user_input = input("Enter the input file name: ")
infile = open(user_input, "r")

col1 = 0 
col2 = 0 
lines = 0
for line in infile : 
    number_str = line.split()       #Split the columns into a list of 2 numbers
    col1 += float(number_str[0])    #First number adds to col1 total
    col2 += float(number_str[1])
    lines += 1                      #Counting lines unnecessary but easy

avg1 = col1 / lines
avg2 = col2 / lines

print(f"The averages are {avg1:.2f} and {avg2:.2f}.")

infile.close()