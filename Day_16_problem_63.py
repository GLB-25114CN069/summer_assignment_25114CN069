# Write a program to Find pair with given sum. 


n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

target=int(input())
found=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("pair found:",arr[i],arr[j])
            found=True

if not found:
    print("no pair found")