// Write a program to Print multiplication table of 
// a given number

#include<stdio.h>
int main()
{
    int n,i,m;
    printf("enter no:");
    scanf("%d",&n);
    for(i=1;i<=10;i++)
    {
        m=n*i;
        printf("%d\n",m);
    }
    return 0;

}