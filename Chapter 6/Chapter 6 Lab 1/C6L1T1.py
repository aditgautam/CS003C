## Adit Gautam
# 1/28/25
# Chapter 6 Lab 1 Task 1
# Linked List functions


#Part A
list1 = [1,2,3,4,5,6]
list1.reverse()                             #Simple
print(list1)

#Part B
list2 = [4,6,8,6,12]
list2 = [i for i in  list2 if i!= 6]        #Automatically removes a 6 if found while sweeping
print(list2)

#Part C THIS IS MATCHING THE FAKE OUTPUT
list3 = [5,10,15,20,200,25,50,20]
list3 = [200 if i == 20 else i for i in list3]
print(list3)

#Part C as following instructions
list3 = [5,10,15,20,200,25,50,20]
for i in range(len(list3)) :
    if list3[i] == 20 :
        list3[i] = 200
        break
print(list3, "(this is the assigned output)")

#Part D
list4a = ["M", "na", "i", "Ke"] 
list4b = ["y", "me", "s", "lly"]

new_list = []                               #Create new empty list

for i in range(len(list4a)) :
    new_list.append(list4a[i] + list4b[i])  #Need to append since list is empty 
print(new_list)