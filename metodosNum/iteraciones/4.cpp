#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

double y(double x){
    return (log(1-x)-pow(x,2));
}

int main(){
    double a=-1, b=-5;
    int n=15;
    double fprima=(y(b)-y(a))/(b-a);
    double alfa=1/fprima;
    double x[15];
    x[0]=b;
    for (int i = 1; i < n; i++)
    {
        x[i]=x[i-1]-alfa*(y(x[i-1]));
        cout<<x[i]<<endl;
    }
    return 0;
    
}