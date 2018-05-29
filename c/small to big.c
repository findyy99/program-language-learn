#include <stdio.h>

int main(void)

{
    int a[10],i,j,temp;
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    for(i=0;i<9;i++)
    {
        for(j=0;j<10;j++)
            
            if (a[j]>a[j+1])
            {
                temp=a[j];a[j]=a[j+1];a[j+1]=temp;
                
            }
    }
    printf("\nthe sorted numbers:\n");
    for(i=0;i<10;i++)
        printf("%3d",a[i]);
    printf("\n");
}