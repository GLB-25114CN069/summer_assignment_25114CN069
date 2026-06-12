# Write a program to Find maximum frequency 
# element. 

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

max_freq = 0
max_element = None

for i in arr:
    freq = arr.count(i)
    
    if freq > max_freq:
        max_freq = freq
        max_element = i

print("Element with maximum frequency:", max_element)
print("Frequency:", max_freq)