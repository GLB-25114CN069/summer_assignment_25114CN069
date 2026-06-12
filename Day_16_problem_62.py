# Write a program to Find missing number in 
# array. 

arr = [1, 2, 3, 5, 6]  # Missing number is 4

n = len(arr) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)