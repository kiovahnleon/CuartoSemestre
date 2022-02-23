#include <stdio.h>
#include <math.h>

int main()
{
    float error;
    float a = 0, b, c = 2;
    float fa, fb, fc;

    error = (c-a)/2;
    b=(a+c)/2;
    printf("%f", b);
    printf("\n");

    while(error >=0.000001){

        fa= pow(M_E,a)-2;
        fb= pow(M_E,b)-2;
        fc= pow(M_E,c)-2;

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

        printf("%f", b);
        printf("\n");

        printf("El resultado es: %f", fb);
        printf("\n");
    }

    return 0;
}
