#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int period_length(int n)
{
    int a_0, a, b, c, b_0, c_0, result = 0;
    a_0 = sqrt(n * 1.0);
    b = b_0 = a_0;
    c = c_0 = n - a_0 * a_0;
    do{
        a = (a_0 + b) / c;
        b = a * c - b;
        c = (n - b * b) / c;
        result++;
    }
    while((b != b_0) || (c != c_0));
    return result;
}

bool isqrt(int x) {
    int y = sqrt(x);
    if (y*y == x)
        return true;
    return false;
}

int main()
{
    int ans = 0;
    for(int i = 2; i <= 10000; ++i)
        if(isqrt(i) == false && period_length(i) % 2 != 0)
            ans++;
    printf("%d", ans);
    return 0;
}
