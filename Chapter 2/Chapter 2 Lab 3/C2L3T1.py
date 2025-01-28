## Adit Gautam
# 1/27/25
# Chapter 2 Lab 3 Task 1
# A program to format a 10 digit phone number

phone_number = str(8884554415)

#Avoid user error, ensure phone number is correct length
assert len(phone_number) == 10, "Phone number did not have the correct number of digits (10), length was" + len(phone_number)

print("The phone number is:", phone_number)

area_code = phone_number[0:3]               #String slicing - takes index values from range 0-3 (but not including 3)
middle_three = phone_number[3:6]
last_four = phone_number[6:10]

final_number = '(' + area_code + ')' + ' ' + middle_three + '-' + last_four

print("The formatted number is:" , final_number)


