#include <bits/stdc++.h>
using namespace std;

int dayofweek(int d, int m, int y)
{
    int yy = y;
    int c = (yy - (y % 100))/100;
    int arr[] = {0, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    (m < 3) ? y = (y % 100) - 1 : y %= 100;
    int ans = (d + (13*arr[m] - 1)/5 + y + (y/4) + (c/4) - (2*c))%7;

    return ans;
}

int main()
{
    int cnt = 0;
    for(int y = 1901; y <= 2000; ++y){
        for(int m = 1; m <= 12; ++m){
            if (dayofweek(1,m,y) == 0)
                cnt++;
        }
    }

    cout << cnt;

    return 0;
}
