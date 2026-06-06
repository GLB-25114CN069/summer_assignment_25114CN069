# Write a program to Print star pyramid. 
#     * 
#    *** 
#   ***** 
#  ******* 
# *********


n = int(input())

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()