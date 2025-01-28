## Adit Gautam
# 1/28/25
# Chapter 4 Lab 3 Task 2
# Collatz Conjecture

# I implemented bogosort in cs2 so I actually like this stuff

from random import randint

stop_counter = 0                        #Initialize stopping time to 0
                                        #Also if we randomly generate 1, then stop timer is 0
n = randint(1,20)                       #Random n between 1 and 20

print("The value of n is", n)

while n != 1 :
    if n % 2 == 0 : 
        n /= 2                          #Half if even
    else :
        n = (3 * n) + 1                 #3n+1 if odd
    print(n)
    stop_counter += 1                   #Outside of the branching so it increments every loop

print("Total stopping time is", stop_counter)
