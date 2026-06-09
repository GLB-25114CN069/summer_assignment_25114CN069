n=int(input("enter no of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)

largest=arr[0]
for i in arr:
    if i>largest:
        largest=i

smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i

print(largest)
print(smallest)