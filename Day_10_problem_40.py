# Write a program to Print character pyramid.
#     A 
#    ABA 
#   ABCBA 
#  ABCDCBA 
# ABCDEDCBA


n = int(input())

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print increasing characters
    for k in range(i):
        print(chr(65 + k), end="")

    # Print decreasing characters
    for k in range(i - 2, -1, -1):
        print(chr(65 + k), end="")

    print()