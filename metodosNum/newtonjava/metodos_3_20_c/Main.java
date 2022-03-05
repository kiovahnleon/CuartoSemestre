package newtonjava.metodos_3_20_c;
import java.math.*;

//Ejercicio 3.20 - c

public class Main {
    public static void main(String[] args) {
        int n = 10; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 0; // Valores estimados = 5,3,0

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.exp(x)-5*Math.pow(x,2));
    }

    public static double fprima(double x){
        return(Math.exp(x)-10*x);
    }
}