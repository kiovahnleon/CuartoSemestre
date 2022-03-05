package newtonjava.metodos_3_18;
import java.math.*;

//Ejercicio 3.18

public class Main {
    public static void main(String[] args) {
        int n = 10; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 4; // Valores estimados = 4,7,10

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.tan(x)-Math.tanh(x));
    }

    public static double fprima(double x){
        return(Math.pow(Math.tan(x), 2) + Math.pow(Math.tanh(x),2));
    }
}