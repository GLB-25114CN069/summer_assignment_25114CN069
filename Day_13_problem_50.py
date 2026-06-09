
n = int(input("Enter number of elements: "))


arr = []
sum=0

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    sum+=num

print(sum)
avg=sum/n
print(avg)