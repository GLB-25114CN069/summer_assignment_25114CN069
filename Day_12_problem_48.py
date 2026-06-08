# Write a program to Write function for perfect number.

def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s += i

    return s == n

n = int(input("Enter a number: "))

if perfect(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")