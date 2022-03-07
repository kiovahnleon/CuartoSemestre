#include <stdio.h>

void main(){
    float suma = 1;
    float total = 0;
    int i = 1;

    for (int i = 0; i < 100; i++)
    {
        total = 0;
        for (int j = 1; j <= 100; j++)
        {
            total = total + 0.00001;
        }
        suma = suma + total;
    }
    printf("hola");
    printf("%f ", suma);
    printf("\n");



}