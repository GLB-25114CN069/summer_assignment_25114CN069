// Write a program to Find product of digits. 

#include<stdio.h>
int main()
{
    int n,prod=1,r;
    printf("enter no:");
    scanf("%d",&n);
    while (n!=0)
    {
        r=n%10;
        prod=prod*r;
        n=n/10;
    }
    printf("%d",prod);
    return 0;
    
}