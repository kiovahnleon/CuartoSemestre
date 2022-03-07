#include <stdio.h>
#include <math.h>

int main()
{
    float error;
    float a = 0, b, c = 1;
    float fa, fb, fc;

    error = (c-a)/2;
    b=(a+c)/2;
    printf("%f", b);
    printf("\n");

    while(error >=0.001){

        fa= a*sin(a)-0.1;
        fb= b*sin(b)-0.1;
        fc= c*sin(c)-0.1;

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

        printf("f(b): %f", fb);
        printf("\n");
    }

    return 0;
}
