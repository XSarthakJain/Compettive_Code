#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int main(int argc, char const *argv[])
{
    int n,i,result=0,rem,base=1;
    n=atoi(argv[1]);
    while(n>0){
        rem=n%2;
        result=result+rem*base;
        n=n/10;
        base=base*2;

    }
    printf("%d\n",result);
    

    return 0;
}
