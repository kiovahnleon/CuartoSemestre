package newtonjava.metodos_3_19;
import java.math.*;

//Ejercicio 3.19

public class Main {
    public static void main(String[] args) {
        int n = 10; //Determina el numero de iteraciones, mas iteraciones = mayor exactitud
        double x0 = 2; // Valor inicial = entre(1,3)

        double a[] = new double[n];
        a[0] = x0;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] - (f(a[i-1]) / fprima(a[i-1]));
            System.out.println(a[i]);
        }

    }

    public static double f(double x){
        return(Math.sin(x)-x+1);
    }

    public static double fprima(double x){
        return(Math.cos(x)-1);
    }
}