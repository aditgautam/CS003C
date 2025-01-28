## Adit Gautam
# 1/28/25
# Chapter 4 Lab 2 Task 2
# Examples using nested looping

n = int(input("Enter n:"))

# two_d_array = [[0] * n for _ in range(n)] 
# # [0] * n creates a row with n number of 0
# # for _ in range n indicates to create n number of rows
# # We now have an NxN matrix to fill values into 

# for i in range(n) :
#     for j in range(n):
#         two_d_array[i][j] = (i+1) * (j+1)                 #Indexing starts at 0 but we want to start at 1

# TOP ROW
print("\n   |" ,end =" ")                                   # New  line,  2 spaces, no newline
for i in range(1, n + 1 )  :                                # Top row, i.e if n = 5, print 1 2 3 4 5
    print(f"{i:3}", end = " ")                              # 3 char spacing
print("\n" + "-" * (n*5))                                   # New line, 4 dashes for each number (SHOULD WORK?)

# Contents of array + row indicator
for i in range(1, n + 1) :                                  #1 to n+1 just makes the declaration of i*j easier
    print(f"{i:2} |", end = " ")
    for j in range(1, n + 1) :
        print(f"{i* j:3}", end = " ")                       #No newline since we want a table 
    print()                                                 #Newline on outer loop iteration





