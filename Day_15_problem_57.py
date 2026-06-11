# Write a program to Reverse array. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

arr.reverse()
print("reverse array: ",arr)