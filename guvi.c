#include<stdio.h>
void main()
{
int a;
printf("enter the number");
scanf("%d",&a);
if(a<0)
{
printf("negative");
}
elseif(a>0)
{
printf("positive");
}
else
{
printf("zero");
}
}