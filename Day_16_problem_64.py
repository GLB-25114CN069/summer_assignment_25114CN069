# Write a program to Remove duplicates from 
# array. 

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

unique_arr=[]
for item in arr:
    if item not in unique_arr:
        unique_arr.append(item)

print("final array:",unique_arr)