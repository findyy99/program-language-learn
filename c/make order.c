#include <stdio.h>

int main(void)

{
    int a[10],i,j,temp;
    printf("请输入10个数字\n");
    for(i=0;i<10;i=i+1)
    {
        printf("第%d个数字: ",i+1);
        scanf("%d",&a[i]);
    }
    for (j=0;j<9;j=j+1)
    {
        for (i=0; i<9;i=i+1)
        {
            if(a[i]>a[i+1])
            {   temp=a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
                
            }
        }
    }
    printf("数字的顺序为:\n");
    for(i=0;i<10;i++)
        printf("%3d",a[i]);
    printf("\n");
}