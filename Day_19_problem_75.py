m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

A = []
transpose = []

print("Enter elements of first matrix:")
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

# transpose of matrix
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[j][i])
    transpose.append(row)

print("transpose of matrix:")
for row in transpose:
    print(*row)