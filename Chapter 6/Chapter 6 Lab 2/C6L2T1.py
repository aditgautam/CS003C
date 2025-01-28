## Adit Gautam
# 1/28/25
# Chapter 6 Lab 2 Task 1
# Finding out if two lists contain the same elements

def sameElements(a,b) :                 #I've implemented bogosort before, if you need me to brute force this I can
    return sorted(a) == sorted(b)       #Sorts the list and then just check if its identical
        

def main() :
    list1 = [11,4,9,16,9,7,4,9,1]
    list2 = [11,1,4,9,16,9,7,4,9]
    
    print("List 1 is", list1)
    print("List 2 is", list2)
    print("The lists contain the same elements: ", sameElements(list1,list2))

main()