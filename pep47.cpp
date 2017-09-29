#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int factor_count(int n){
   int c = 0;
    for(int i = 2; n != 1; i++) {
        if(n % i == 0) {
            c++;
            while(n % i == 0)
                n /= i;
		}
	}
	return c;
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    int pattern[] = {4,4,4,4};

    for (int i = 1; i <= n; ++i)
        arr[i] = factor_count(i);

    int *ptr;
    ptr = search(arr, arr + n, pattern, pattern + 4);

    if (ptr == arr + n)
        cout << "No match found";
    else
        cout << ptr - arr;
    return 0;
}
