# Write a program to Merge arrays. 

n1 = int(input("Enter number of elements in first array: "))
arr1 = []

print("Enter elements of first array:")
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Enter number of elements in second array: "))
arr2 = []

print("Enter elements of second array:")
for i in range(n2):
    arr2.append(int(input()))

merged_arr = arr1 + arr2

print("Merged array:", merged_arr)