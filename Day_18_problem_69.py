# Write a program to Bubble sort. 


n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)