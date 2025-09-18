#include<stdio.h>

void main()
{
    int a[10][10],b[10][10],m,n,c[10][10];
    int i,j;

    printf("enter the rows and column");
    scanf("%d%d",&m,&n);

    printf("enter the a array elemets ");
    for(i=0;i<m;i++)
    {   
        for (j=0 ;j<n;j++)
        {   
            printf("hello");
            scanf("%d",&a[i][j]);
        }
    }
    printf("enter the b array elemets ");
    for(i=0;i<m;i++)
    {   
        for (j=0 ;j<n;j++)
        {
            scanf("%d",&b[i][j]);
        }
    }
    printf("the dsilpaly ");
    for(i=0;i<m;i++)
    {   
        for (j=0 ;j<n;j++)
        {   printf("%d",a[i][j]);}
    }
    for(i=0;i<m;i++)
    {   
        for (j=0 ;j<n;j++)
        {   printf("%d",b[i][j]);}
    }

}