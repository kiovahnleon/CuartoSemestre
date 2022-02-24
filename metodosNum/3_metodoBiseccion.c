#include <stdio.h>
#include <math.h>

int main()
{
    double error;
    double a = 0, b, c = M_PI;
    double fa, fb, fc;

    error = (c-a)/2;
    b=(a+c)/2;
    printf("%f", b);
    printf("\n");

    while(error >=0.005){

        fa= tan(a)-3.5;
        fb= tan(b)-3.5;
        fc= tan(c)-3.5;

        if(fb>=0&&fa<0||fb<0&&fa>=0){
            a=a;
            c=b;
        }
        else{
            a=b;
            c=c;
        }

        b=(a+c)/2;

        error = error/2;

        printf("La raiz es: %f", b);
        printf("\n");

        printf("f(b) %f", fb);
        printf("\n");
    }

    return 0;
}
