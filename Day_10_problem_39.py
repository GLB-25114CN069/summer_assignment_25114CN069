# Write a program to Print number pyramid. 
#     1 
#    121 
#   12321 
#  1234321 
# 123454321 


n = int(input())

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end="")

    # Print decreasing numbers
    for k in range(i - 1, 0, -1):
        print(k, end="")

    print()