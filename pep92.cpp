#include <bits/stdc++.h>
using namespace std;

int digit_square(int n)
{
    int sum = 0;
    while(n > 0){
        int r = n % 10;
        sum += r*r;
        n /= 10;
    }
    return sum;
}

int chain(int n)
{
    int m = digit_square(n);

    while(m != 1 && m != 89)
        m = digit_square(m);
    return m;
}

int main()
{
    int n = 10000000;
    int cnt = 0;
    for (int i = 1; i <= n; ++i){
        if(chain(i) == 89)
            cnt++;
    }

    cout << cnt;
    return 0;
}
