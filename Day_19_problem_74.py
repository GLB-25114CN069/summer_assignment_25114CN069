m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of first matrix:")
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

print("Enter elements of second matrix:")
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)

Sub = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] - B[i][j])
    Sub.append(row)

print("Subtraction of matrices:")
for row in Sub:
    print(*row)