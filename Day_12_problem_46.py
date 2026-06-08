# Write a program to Write function for 
# Armstrong.


def armstrong(n):
    digits = len(str(n))
    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    return sum == n

n = int(input("Enter a number: "))
print(armstrong(n))