#include<stdio.h>
#include<stdlib.h>
int main(int argc, char const *argv[])
{
    /* code */
    int i,f=1;
    for(i=1;i<=atoi(argv[1]);i++){
        f=f*i;
    }
    printf("%d",f);
    return 0;
}
