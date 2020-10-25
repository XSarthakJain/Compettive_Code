#include<stdio.h>
#include<math.h>
int main(int argc, char const *argv[])
{
    
    float l,b;
    
    l=atof(argv[1]);
    b=atof(argv[2]);
    
    printf("Length of the Hypotenous = %f",sqrt((l*l)+(b*b)));
   
   
    return 0;
}
