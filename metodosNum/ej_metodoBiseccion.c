#include <stdio.h>
#include <math.h>

int main()
{
    printf("Kiovahn Leon");

    double Err;
    double A = 0;
    double B;
    double C = 2;
    double FdeA;
    double FdeB;
    double FdeC;

    Err = (C-A)/2;
    B=(A+C)/2;

    while(Err >=0.001){

        FdeA= pow(M_E,A)-2;
        FdeB= pow(M_E,B)-2;
        FdeC= pow(M_E,C)-2;

        if(FdeB>=0&&FdeA<0||FdeB<0&&FdeA>=0){
            A=A;
            C=B;
        }
        else{
            A=B;
            C=C;
        }

        B=(A+C)/2;

        Err = Err/2;

        printf("f(b): %f", B);
        printf("\n");

        printf("El resultado es: %f", FdeB);
        printf("\n");
    }

    return 0;
}
