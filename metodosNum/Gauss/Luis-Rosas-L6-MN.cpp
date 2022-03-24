
#include<stdio.h>
#include<stdlib.h>

float rellenaMatriz(float M[20][20], int tam)
{
	int i, j;
	
	for(i=0; i<tam; i++)
	{
		for(j=0; j<=tam; j++)
		{
			printf("\nIngresa el valor de M[%i][%i]: ", i+1, j+1);
			scanf("%f", &M[i][j]);
		}
	}	
}

void imprimeMatriz(float M[20][20], int tam)
{
	int i, j;
	printf("\n");
	for(i=0; i<tam; i++)
	{
		for(j=0; j<=tam; j++)
		{
			printf("M[%i][%i]: %.2f\t",i+1, j+1, M[i][j]);
		}
		printf("\n");
	}
}


float GaussJordan(float M[20][20], int tam)
{
	int I, i, j, k;
	float Piv, aux;
	
	for(I=0; I<tam; I++)
	{
		Piv=M[I][I];
		for(j=0; j<=tam; j++)
		{
			M[I][j]=M[I][j]/Piv;
		}
		for(i=0; i<tam; i++)
		{
			if(i!=I)
			{	
				aux=M[i][I];				
				for(j=0; j<=tam; j++)
				{
					M[i][j]=M[i][j]-(aux*M[I][j]);	
				}
			}		
		}
	}
}	



int main ()
{
	int tam, i, j;
	printf("Ingresa el tama%co de la matriz cuadrada: ", 164);
	scanf("%d", &tam);
	float M[20][20];
	rellenaMatriz(M, tam);
	imprimeMatriz(M, tam);
	GaussJordan(M, tam);
	imprimeMatriz(M, tam);
	
	return 0;
}
