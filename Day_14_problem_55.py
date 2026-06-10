# Write a program to Second largest element. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

arr.sort()

print("Second largest element =", arr[-2])