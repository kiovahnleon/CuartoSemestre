#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

double y(double x){
    return (tan(0.1*x)-9.2*exp(-x));
}

int main(){
    double a=3, b=4;
    int n=7;
    double fprima=(y(b)-y(a))/(b-a);
    double alfa=1/fprima;
    double x[7];
    x[0]=b;
    for (int i = 1; i < n; i++)
    {
        x[i]=x[i-1]-alfa*(y(x[i-1]));
        cout<<x[i]<<endl;
    }
    return 0;
    
}