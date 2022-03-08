#include <stdio.h>
#include <math.h>

int main()
{
    float error;
    float a = 1, b, c = 2;
    float fa, fb, fc;

    error = (c-a)/2;
    b=(a+c)/2;
    printf("%f", b);
    printf("\n");

    while(error >=0.001){

        fa= pow(a,2)-.9*a-1.52;
        fb= pow(b,2)-.9*b-1.52;
        fc= pow(c,2)-.9*c-1.52;

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

        printf("%f", fb);
        printf("\n");
    }

    return 0;
}
