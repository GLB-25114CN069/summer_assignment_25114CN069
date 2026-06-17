# Write a program to Binary search. 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Element found

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1  # Element not found


n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

target=int(input("enter element to be searched:"))

result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")