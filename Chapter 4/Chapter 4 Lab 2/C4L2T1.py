## Adit Gautam
# 1/28/25
# Chapter 4 Lab 2 Task 1
# Examples using for looping

# Sum of even numbers between 2 and 100

sum_evens = 0 

for i in range (2, 101) :
    if i % 2 == 0 :                     #Only evens
        sum_evens += i
print("Sum of even numbers between 2 and 100:" , sum_evens)
# Sum of all squares between 1 and 100

sum_squares = 0

for i in range(1, 101) :                #Range: Start at 1, go UP TO (dont include) 101
    sum_squares += (i**2)
print("Sum of squares between 1 and 100:", sum_squares)

# All powers of 2 from 20 up to 30
print("Powers of @ from 20 up to 30")
for i in range(20, 31) :
    print(2 ** i)

