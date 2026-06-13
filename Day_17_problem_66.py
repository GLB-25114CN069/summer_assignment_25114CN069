# Write a program to Union of arrays. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

union_of_arr=[]
for i in arr:
    if i not in union_of_arr:
        union_of_arr.append(i)

print(union_of_arr)