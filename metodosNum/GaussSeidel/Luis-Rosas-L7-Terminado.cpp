#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void menu ();

void Jacobi();
void Seiden();

void rellenaMatriz(float [][20], int);
int dominante(float [][20], int);
void Xr(float [][20], int, float [], float []);
void XrG(float [][20], int, float []);
void ImprimeMatr(float [][20], int);
void CambiaRen(float [][20], int, int);

int main ()
{
	
	menu ();
	
	return 0;
}

/*MENU DE OPCIONES*/
void menu ()
{
	int op;
	do{
		system("cls");
		printf("- MENU - \n\n1-Metodo de Jacobi \n2-Metodo de Gauss-Seidel \n3-Salir \n\nElige un opcion: ");
		scanf("%d", &op);
	
		switch(op)
		{
			case 1: Jacobi();
				break;
			case 2: Seiden();
				break;
			case 3: break;
			default: printf("\nPorfavor escribir un numero dentro del rango");
				break;
		}
		printf("\n\n");
		system("pause");
		
	}while(op!=3);
}

/*METODO DE JACOBI*/
void Jacobi()
{
	system("cls");
	int ite=1, tam, i, ren=0, banJa=0, ban, contador=0;
	float M[20][20]={{0}}, ep, Xant[20]={0}, Xact[20]={0}, epc[20]={0};
	printf("- METODO DE Jacobi - 	\n\nIngresa el tama%co de la matriz cuadrada: ", 164);
	scanf("%d", &tam);
	printf("\nIngresa el error porcentual deseado: ");
	scanf("%f", &ep);	
	rellenaMatriz(M, tam);
	printf("\nMATRIZ ORIGINAL");
	ImprimeMatr(M, tam);
	printf("\n");
	do{
		
		if(dominante(M, tam)==1)
		{
			banJa=1;
			do{	
			printf("\n******************************************************************************** \nIteracion %d\n", ite);
			Xr(M, tam, Xact, Xant);
			for(i=0; i<tam; i++)
			{
				epc[i]=fabs(((Xact[i]-Xant[i])/Xact[i])*100);
				printf("\nX%d = %.2f \t\tEPC = %.2f%%", i+1, Xact[i], epc[i]);
				Xant[i]=Xact[i];
			}
			
			ban=0;
			i=0;
			do{
				if(epc[i]>ep)
					ban=1;
				i++;
			}while(ban==0 && i<tam);
			ite++;
			
			}while(ban==1);
		}
		else
		{
			printf("NO se puede aplicar el metodo porque la matriz no es diagonalmente dominante \n\nSe cambiara los renglones: ");
			CambiaRen(M, tam, ren);
			ImprimeMatr(M, tam);
			ren++;	
			if(ren==tam-1)
			{
				ren=0;
			}
			contador++;
			
		}
	}while(banJa==0 && contador<20);
	if(contador==20)
	{
		system("cls");
		printf("\n\nNo aplica el metodo para esta matriz\n\n");
		system("pause");
	}
}

/*METODO DE SEIDEL*/
void Seiden()
{
	system("cls");
	int ite=1, tam, i, ren=0, banJa=0, ban, contador=0;
	float M[20][20]={{0}}/*{{3,12,-1,-2},{11,-4,3,-3},{-3,-2,-12,-2}}*/, ep, Xant[20]={0}, Xact[20]={0}, epc[20]={0};
	printf("- METODO DE GAUSS-SEIDEL - 	\n\nIngresa el tama%co de la matriz cuadrada: ", 164);
	scanf("%d", &tam);
	printf("\nIngresa el error porcentual deseado: ");
	scanf("%f", &ep);	
	rellenaMatriz(M, tam);
	printf("\nMATRIZ ORIGINAL");
	ImprimeMatr(M, tam);
	printf("\n");
	do{
		
		if(dominante(M, tam)==1)
		{
			banJa=1;
			do{	
			printf("\n******************************************************************************** \nIteracion %d\n", ite);
			XrG(M, tam, Xact);
			for(i=0; i<tam; i++)
			{
				epc[i]=fabs(((Xact[i]-Xant[i])/Xact[i])*100);
				printf("\nX%d = %.2f \t\tEPC = %.2f%%", i+1, Xact[i], epc[i]);
				Xant[i]=Xact[i];
			}
			
			ban=0;
			i=0;
			do{
				if(epc[i]>ep)
					ban=1;
				i++;
			}while(ban==0 && i<tam);
			ite++;
			
			}while(ban==1);
		}
		else
		{
			printf("NO se puede aplicar el metodo porque la matriz no es diagonalmente dominante \n\nSe cambiara los renglones: ");
			CambiaRen(M, tam, ren);
			ImprimeMatr(M, tam);
			ren++;	
			if(ren==tam-1)
			{
				ren=0;
			}
			contador++;
			
		}
	}while(banJa==0 && contador<20);
	if(contador==20)
	{
		system("cls");
		printf("\n\nNo aplica el metodo para esta matriz\n\n");
		system("pause");
	}
}



/*RELLENA LA MATRIZ DE NxN*/
void rellenaMatriz(float M[][20], int tam)
{
	int i, j;
	printf("\nRellena la matriz de %dx%d\n\n", tam, tam);
	for(i=0; i<tam; i++)
	{
		for(j=0; j<=tam; j++)
		{
			if(j==tam)
				printf("Resultado: ", i, j);
			else
				printf("M[%d][%d]: ", i, j);
			scanf("%f", &M[i][j]);
		}
		printf("\n");
	}
}

/*VERIFICA QUE LA MATRIZ SEA DIAGONALMENTE DOMINANTE*/
int dominante(float M[][20], int tam)
{
	int i, j;
	float piv, sum;
	
	for(i=0; i<tam; i++)
	{
		piv=M[i][i];
		sum=0;
		for(j=0; j<tam; j++)
		{
			if(i!=j)
			{
				sum+=fabs(M[i][j]);
			}
		}
		if(fabs(M[i][i])<sum)
			return 0;
	}
	return 1;
}
/*CALCULA EL XR DEL METODO DE JACOBI*/
void Xr(float M[][20], int tam, float Xact[], float Xant [])
{
	int i, j;
	float sp;
	
	for(i=0; i<tam; i++)
	{
		sp=0;
		for(j=0; j<tam; j++)
		{
			if(i!=j)
				sp+=M[i][j]*Xant[j];
		}
		Xact[i]=(M[i][tam]-sp)/M[i][i];
	}
}
/*CALCULA EL XR DEL METODO DE GAUSS-SEIDEL*/
void XrG(float M[][20], int tam, float Xact[])
{
	int i, j;
	float sp;
	
	for(i=0; i<tam; i++)
	{
		sp=0;
		for(j=0; j<tam; j++)
		{
			if(i!=j)
				sp+=M[i][j]*Xact[j];
		}
		Xact[i]=(M[i][tam]-sp)/M[i][i];
	}
}

/*CAMBIA LOS RENGLONES DE LA MATRIZ POR SI NO ES DIAGONALMENTE DOMINANTE*/
void CambiaRen(float M[][20], int tam, int ren)
{
	int i, j; 
	float Raux[tam+1];

	for(i=0; i<tam+1; i++)
	{
			Raux[i]=M[ren+1][i];
			M[ren+1][i]=M[ren][i];
			M[ren][i]=Raux[i];	
	}
}

/*IMPRIME LA MATRIZ*/
void ImprimeMatr(float M[][20], int tam)
{
	int i, j;
	printf("\n");
	for(i=0; i<tam; i++)
	{
		for(j=0; j<tam+1; j++)
		{
			printf("%.2f\t", M[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}
