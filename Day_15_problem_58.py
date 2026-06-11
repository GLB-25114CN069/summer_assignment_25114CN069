# Write a program to Rotate array left. 

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

d = int(input("Enter the number of positions to rotate left: "))

# Handle cases where d > n
d = d % n

# Left rotation
arr = arr[d:] + arr[:d]

print("Array after left rotation:")
print(arr)