package newtonjava.metodos_3_20_d;
import java.math.*;

//Ejercicio 3.20 - d

public class Main {
    public static void main(String[] args) {
        int n = 10; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 5; // Valores estimados = 5

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.pow(x,3)+2*x-1);
    }

    public static double fprima(double x){
        return(3*Math.pow(x,2)+2);
    }
}