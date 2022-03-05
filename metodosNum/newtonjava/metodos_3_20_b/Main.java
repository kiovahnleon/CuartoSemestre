package newtonjava.metodos_3_20_b;
import java.math.*;

//Ejercicio 3.20 - b

public class Main {
    public static void main(String[] args) {
        int n = 30; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 1; // Valores estimados = 1 , 0.1

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.log(1+x)-Math.pow(x,2));
    }

    public static double fprima(double x){
        return(-2*Math.pow(x,2)-2*x+1)/x+1;
    }
}