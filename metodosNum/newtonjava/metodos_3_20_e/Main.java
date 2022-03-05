package newtonjava.metodos_3_20_e;
import java.math.*;

//Ejercicio 3.20 - e

public class Main {
    public static void main(String[] args) {
        int n = 100; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 4; // Valores estimados = 4

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.sqrt(x+2)-x);
    }

    public static double fprima(double x){
        return((-2*Math.sqrt(x+2)+1)/2*Math.sqrt(x+2));
    }
}