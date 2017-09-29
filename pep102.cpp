#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int arr[1000][6] = {{0}};

double area(int x1, int y1, int x2, int y2, int x3, int y3)
{
   return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0);
}

bool isInside(int x1, int y1, int x2, int y2, int x3, int y3)
{
   /* Calculate area of triangle ABC */
   double A = area (x1, y1, x2, y2, x3, y3);

   /* Calculate area of triangle PBC */
   double A1 = area (0, 0, x2, y2, x3, y3);

   /* Calculate area of triangle PAC */
   double A2 = area (x1, y1, 0, 0, x3, y3);

   /* Calculate area of triangle PAB */
   double A3 = area (x1, y1, x2, y2, 0, 0);

   /* Check if sum of A1, A2 and A3 is same as A */
   return (A == A1 + A2 + A3);
}

int main()
{
    FILE* fp;
    fp = fopen("C:\\Users\\hp lap\\Desktop\\College\\pep_102 data.txt","r");

    int x1, y1, x2, y2, x3, y3, ans = 0;

    for(int i = 0; i < 1000; ++i){
        fscanf(fp,"%d, %d, %d, %d, %d, %d", &x1, &y1, &x2, &y2, &x3, &y3);
        arr[i][0] = x1;
        arr[i][1] = y1;
        arr[i][2] = x2;
        arr[i][3] = y2;
        arr[i][4] = x3;
        arr[i][5] = y3;
    }

    fclose(fp);

    for(int i = 0; i < 1000; ++i){
        if(isInside(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4], arr[i][5]) == true)
            ans++;
    }

    printf("%d", ans);

    return 0;
}
