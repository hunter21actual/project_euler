#include<cstdio>
#include<cmath>
using namespace std;

int main()
{
    FILE* fp;
    fp = fopen("C:\\Users\\hp lap\\Desktop\\College\\pep_99 data.txt","r");

    double x, y, MAX = 0.;
    int i, sol;

    for(i = 1; i <= 1000; ++i){
        fscanf(fp,"%lf, %lf", &x, &y);
        y *= log(x);
        if(y > MAX){
            MAX = y;
            sol = i;
        }
    }
    fclose(fp);

    printf("%d\n",sol);
    return 0;
}
