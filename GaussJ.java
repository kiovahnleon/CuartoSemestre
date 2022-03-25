public class GaussJ {
    public static void main(String[] args) {
        double a[], x[][]={
            {1,1,1,1,-2,2},
            {2,-1,3,4,5,-1},
            {3,2,-2,-2,1,4}
        };

        for(int n=0;n < x.length; n++){
            a = x[n].clone();

            for(int h = 0; h< a.length ; h++) a[h] = a[h]/x[n][n];

            x[n] = a.clone();
            printMatriz(x);

            for(int k = 0; k < x.length ; k++){
                if(n!=k){
                    double aux[] = arrayEscalar(a.clone(),(-1*x[k][n]));
                    for(int i = 0 ; i < x[0].length ; i++){
                        x[k][i] += aux[i];
                    }
                    printMatriz(x);
                }
            }
        }        

    }
    
    public static double[] arrayEscalar(double array[], double escalar) {
        for (int i = 0; i < array.length; i++)
            array[i] *= escalar;
        return array;
    }

    public static void printMatriz(double x[][]) {
        System.out.println("------------------\n");
        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < x[0].length; j++)
                System.out.println(x[i][j] + ", ");
            System.out.println();
        }
        System.out.println();
        System.out.println("----------------------");
    }
}
