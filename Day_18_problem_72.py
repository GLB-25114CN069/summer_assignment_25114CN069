# Write a program to Sort array in descending 
# order. 

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))


for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Array in descending order:")
print(arr)