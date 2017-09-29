#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

int main()
{
    int arr[100][100] = {{0}};


    ifstream file;
    file.open("C:\\Users\\hp lap\\Desktop\\College\\p067_triangle.txt");

    if(file.is_open()){
        while(!file.eof()){
            for(int i = 0; i < 100; i++){
                for(int j = 0; j <= i; j++){
                    //level[i][j] = ???
                    file >> arr[i][j];
                }
            }
        }
    }

    file.close();

    for(int i = 98; i >= 0; i--){
        for(int j = 0; j <= i; ++j){
            arr[i][j] = max(arr[i][j] + arr[i+1][j], arr[i][j] + arr[i+1][j+1]);
        }
    }

    cout << arr[0][0];
    return 0;
}
