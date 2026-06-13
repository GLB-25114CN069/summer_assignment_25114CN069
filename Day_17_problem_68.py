# Write a program to Find common elements. 

n = int(input("Enter number of elements: "))

arr1 = []
arr2 = []

print("Enter elements of first array:")
for i in range(n):
    arr1.append(int(input()))

print("Enter elements of second array:")
for i in range(n):
    arr2.append(int(input()))

common_elements = []

for i in arr1:
    if i in arr2 and i not in common_elements:
        common_elements.append(i)

print("Common elements:", common_elements)