## Adit Gautam
# 1/28/25
# Chapter 6 Lab 2 Task 2
# 2D arrays (lists?)

def is_magic_square(matrix) :   #Returns Boolean. Pass in a 2d array
    n = len(matrix)             #Even if this is a 2d array a square is fine
    expected_sum = sum(matrix[0])

    for row in matrix :         #For each row in the matrix we will take the sum and check against
        if sum(row) != expected_sum :
            return False        #Early return. If the rows aint adding, nothing will
    
    for col in range(n) :
        col_sum = 0
        for row in range(n) :
            col_sum += matrix[row][col]
        if col_sum != expected_sum :
            return False
    
    diag1_sum = 0

    for i in range(n) :                 #Will start adding up 0,0 1,1 2,2
        diag1_sum += matrix[i][i]
    
    if diag1_sum != expected_sum :
        return False
    
    diag2_sum = 0

    for i in range(n) :
        diag2_sum += matrix[i][n-i-1]   #Adds 0,3 1,2 2,1 3,0
    
    if diag2_sum != expected_sum :
        return False
    
    return True                         #Once we check everything, we can return true

def main() :

    magic_square = [
        [16,3,2,13],
        [5,10,11,8],
        [9,6,7,12],
        [4,15,14,1]
    ]

    for row in magic_square : 
        for num in row : 
            print(f"{num:5}", end = "")
        print()
    
    if is_magic_square(magic_square) :
        print("It is a magic square.")
    else :
        print("It is not a magic square")

main()
        