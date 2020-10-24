#include<stdio.h>
#include<conio.h>
int main(){
    float l,b;
    printf("\nEnter Length of 2 Side of triangle");
    scanf("%d %d",&l,&b);
    printf("Length of the Hypotenous = ",sqrt((l*l)+(b*b)));
    getch();
    return 0;
}