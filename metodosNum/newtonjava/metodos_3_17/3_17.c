#include <stdio.h>
#include <math.h>



int main()
    {
        int n = 10;   // Numero de iteraciones
        float x0 = 2; // Valores estimados = 2,5,8

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++)
        {
            a[i] = a[i - 1] - (f(a[i - 1]) / fprima(a[i - 1]));
            System.out.println(a[i]);
        }
    }


double f(double x)
    {
        return (math.cos(x) * M_cosh(x) + 1);
    }

double fprima(double x)
    {
        return (M_cos(x) * M_sinh(x) - M_sin(x) * M_cosh(x));
    }
}