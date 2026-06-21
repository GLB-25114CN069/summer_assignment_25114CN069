m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

A = []

print("Enter elements of first matrix:")
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

sum=0
for i in range(m):
    for j in range(n):
        if i==j:
            sum=sum+A[i][j]

print("sum=" , sum)
