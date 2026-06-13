# Write a program to Intersection of arrays.



n = int(input("Enter number of elements: "))

arr1 = []
arr2 = []

for i in range(n):
    arr1.append(int(input()))

for i in range(n):
    arr2.append(int(input()))

intersection_of_arr = []

for i in arr1:
    for j in arr2:
        if i == j and i not in intersection_of_arr:
            intersection_of_arr.append(i)

print("Intersection of arrays:", intersection_of_arr)

