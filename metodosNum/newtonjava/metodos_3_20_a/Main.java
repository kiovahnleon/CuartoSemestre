package newtonjava.metodos_3_20_a;
import java.math.*;

//Ejercicio 3.20 - a

public class Main {
    public static void main(String[] args) {
        int n = 10; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 1; // Valores estimados = 1,3

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }
    }

    public static double f(double x){
        return(0.5*Math.exp(x/3)-Math.sin(x));
    }

    public static double fprima(double x){
        return((Math.exp(x/3)-6*Math.cos(x))/6);
    }
}