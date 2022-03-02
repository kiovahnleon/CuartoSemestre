#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

double y(double x){
    return (0.5*exp((x/3))-sin(x));
}

int main(){
    double a=1.8, b=2;
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