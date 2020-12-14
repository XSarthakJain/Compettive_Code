#include<stdio.h>
#include<math.h>
int main(int argc, char const *argv[])
{
    int i,temp;
    for(i=1;i<argc;i++){
        temp=atof(argv[i]);
        printf("%d\n",temp);
    }
    return 0;
}
