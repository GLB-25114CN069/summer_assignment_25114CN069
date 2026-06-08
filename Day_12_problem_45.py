# Write a program to Write function for 
# palindrome. 


def palindrome(a):
    if str(a)==str(a)[::-1]:
        return True
    else:
        return False
    
n=str(input())
print(palindrome(n))