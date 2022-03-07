package newtonjava.metodos_3_17;
import java.math.*;

//Ejercicio 3.17

public class Main {
    public static void main(String[] args) {
        int n = 10; // Numero de iteraciones
        float x0 = 2; // Valores estimados = 2,5,8

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / F_(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.cos(x)*Math.cosh(x)+1);
    }

    public static double F_(double x){
        return(Math.cos(x)*Math.sinh(x)-Math.sin(x)*Math.cosh(x));
    }
}