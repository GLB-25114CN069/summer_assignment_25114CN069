# Write a program to Rotate array right. 

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

d = int(input("Enter number of positions to rotate right: "))

d = d % n

arr = arr[-d:] + arr[:-d]

print("Array after right rotation:")
print(arr)