#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[8] = {1,2,5,10,20,50,100,200};
    int dp[201][8];

    for(int i = 0; i < 201; ++i){
        for(int j = 0; j < 8; ++j){
            if(i == 0)
                dp[i][j] = 1;
            else if(j == 0){
                if(i % arr[j] == 0)
                    dp[i][j] = 1;
                else
                    dp[i][j] = 0;
            }
            else if(arr[j] > i)
                dp[i][j] = dp[i][j-1];
            else
                dp[i][j] = dp[i - arr[j]][j] + dp[i][j-1];

        }
    }

    cout << dp[200][7];

    return 0;
}
