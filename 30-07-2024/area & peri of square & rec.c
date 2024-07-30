#include<stdio.h>
int main()
{
    int a,area,peri;
    printf("enter the length");
    scanf("%d",&a);
    area=a*a;
    peri=4*a;
    printf("\narea of square %d",area);
    printf("\nperimeter of square %d",peri);
    {
    int b,c,area,peri;
    printf("\nenter the length");
    scanf("%d",&b);
    printf("\nenter the breadth");
    scanf("%d",&c);
    area=b*c;
    peri=2*(b+c);
    printf("\narea of rectangle %d",area);
    printf("\nperimeter of rectangle %d",peri);
    }
}
