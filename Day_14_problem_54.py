# Write a program to calculate the Frequency of an element.


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter element whose frequency is to be found: "))

count = 0

for i in arr:
    if i == key:
        count += 1

print("Frequency of", key, "=", count)