#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

float y(float x){
    return (pow(x,2)+exp(x)-2)/3;
}

int main(){
    int n=7;
    float x[7];
    x[0]=0;
    for (int i = 1; i < n; i++)
    {
        x[i]=y(x[i-1]);
        cout<<x[i]<<endl;
    }
    return 0;
    
}