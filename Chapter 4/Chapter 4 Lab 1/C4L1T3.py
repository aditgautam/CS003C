## Adit Gautam
# 1/28/25
# Chapter 4 Lab 1 Task 1
# Program to find data regarding grades

total_sum = 0                                   #Summation of all grades
counter = 0                                     #For calculating average
max_grade = -2                                  #Keeping track of max and min, wont say 0 since -1 is terminator
min_grade = 120                                 #Arbitrary value, but grades can be over 100
passing = 0
failing = 0


grade_input = int(input("Enter a grade or -1 to finish:"))

while grade_input != -1 :
    if(grade_input > max_grade) :               #If the input is bigger than the last max, update max
        max_grade = grade_input
    if(grade_input < min_grade ) :
        min_grade = grade_input                 #Same
    
    if(grade_input >= 70) :
        passing +=1                             #Increment passing counter
    if(grade_input < 70 ) :
        failing +=1                             #Same
    total_sum += grade_input                  
    counter += 1 
    grade_input = int(input("Enter a grade or -1 to finish:"))

average = (total_sum / counter)

print("The average grade is %.2f" % average)
print("Number of passing grades is %d" % passing)
print("Number of failing grades is %d" % failing)
print("The maximum grade is %.2f" % max_grade)
print("The minimum grade is %.2f" % min_grade)