#include<cstdio>
#include <iostream>
#include<cmath>
using namespace std;

bool rev(int n)
{
    long long num = n;

    int r = 0;
    while(n > 0){
        r = 10*r + (n % 10);
        n /= 10;
    }
    num = num + r;

    long long c = num;

    int cnt = 0;
    while(c > 0){
        cnt++;
        c /= 10;
    }

    int odd = 0;
    while(num > 0){
        if((num % 10) % 2 != 0)
            odd++;
        num /= 10;
    }

    if(odd == cnt)
        return true;
    else
        return false;
}

int main()
{
    int ans = 0;
    for(int i = 1; i < 100000000; ++i){
        if((i%10) !=0 && rev(i) == true)
            ans++;
    }
    cout << ans;
    return 0;
}
