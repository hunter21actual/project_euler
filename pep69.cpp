#include <iostream>
using namespace std;

int phi(int n){
    int result = n;
    for(int i = 2; i*i <= n; ++i)
        if(n % i == 0){
            while(n % i == 0)
                n /= i;
            result -= result/i;
        }
    if(n > 1)
        result -= result/n;
    return result;
}

int main(){
    int LIM = 1000000;
    float* arr = new float[LIM];
    for(int i = 1; i <= LIM; ++i){
        float n = i;
        arr[i-1] = n/phi(n);
    }

    float largest = 0;
    for (int i = 0; i < LIM; ++i){
        if(arr[i] > largest)
            largest = arr[i];
    }

    for (int i = 0; i < LIM; ++i){
        if(arr[i] == largest)
            cout << i + 1 << " ";
    }

    return 0;
}
