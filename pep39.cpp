#include<cstdio>
#include <iostream>
#include<cmath>
using namespace std;

int arr[1001] = {0};

int main()
{
    for(int i = 3; i < 500; ++i){
        for(int j = i + 1; j < 500; ++j){
            for(int k = j + 1; k < 500; ++k){
                if(i + j + k <= 1000 and i*i + j*j == k*k)
                    arr[i+j+k]++;
            }
        }
    }
    int ans = -20;
    int index = -10;
    for(int i = 0; i < 1001; ++i){
        if(arr[i] > ans){
            ans = arr[i];
            index = i;
        }
    }

    printf("%d %d", ans, index);
    return 0;
}
