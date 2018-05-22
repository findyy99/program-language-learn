/*求数列中最大数，和位置*/
#include <stdio.h>
int main(void)
{
    int a[10],i,imax = 0,imin = 0,d,x;
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    d=x=0;
    for(i=1;i<10;i++)
    {
        if(a[i]>imax)
        {
            imax=a[i];d=i;
        }
        if(a[i]<imin)
        {
            imin=a[i];x=i;
            
        }
    }
    
    printf("imax=%5d,d=%3d\nimin=%5d,x=%3d\n",imax,d,imin,x);
    
    
}