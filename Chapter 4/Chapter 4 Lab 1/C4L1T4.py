## Adit Gautam
# 1/28/25
# Chapter 4 Lab 1 Task 1
# Program to find average of all positive numbers divisible by 3

#COUNTERS INITIALIZED TO 0 - FOR AVERAGE
counter = 0
total_sum = 0

repeat = True                           #Whatever boolean flag requirement

while repeat : 
    user_input = int(input("Enter any positive integer or a negative to stop:"))
    if user_input < 1 : 
        repeat = False
        break                           #I THINK YOU NEED A BREAK STATEMENT? 
    if user_input % 3 == 0 : 
        total_sum += user_input
        counter +=1

average = total_sum / counter

print("The average of the numbers divisible by three is: %.1f"% average)    #Silly formatting3