#include<stdio.h>
void a(int b)
{
   int area;
   area = b*b;
   printf("Area of Square : %d", area);
}
void main()
{
   int side;

   printf("\nEnter the Length of Side : ");
   scanf("%d", &side);

   a(side);
}
