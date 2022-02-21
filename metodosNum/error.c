#include <stdio.h>

void main(){
    float suma = 1;
    int i = 1;

    for (int i = 0; i < 10000; i++)
    {
        suma = suma + 0.00001;
    }
    printf("%f",suma);


}