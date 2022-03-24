public class GaussK{
    public static void main(String[] args) {
        int n=3;
        double factor =0;

        double b[] = {-1.0, 12.0, 0.0};
        double a[][] ={ { 2.0 , 1.0 , -3.0 }, 
                        { -1.0 , 3.0, 2.0},
                        { 3.0, 1.0, -3.0} } ;
        for (int k = 0; k < n-1; k++){
            for(int i = k+1; i < n; i++){
                factor = a[i][k]/a[k][k];

                for(int j = k; j < n; j++){
                    a[i][j]=a[i][j]-(factor)*a[k][j];
                }
                b[i]=b[i]-(factor)*b[k];
            }
        }

        double sum;
        double x[] = new double[n];
        x[n-1]=b[n-1]/a[n-1][n-1];
        
        for (int i = n-2; i >= 0; i--){
            sum=0;
            for (int j = i+1; j<n; j++){
                sum=sum-a[i][j]*x[j];
            }
            x[i]=(b[i]+sum)/a[i][i];
        }

        for (int i=0; i < a.length; i++) {
            System.out.print("|");
            for (int y=0; y < a[i].length; y++) {
              System.out.print (a[i][y]);
              if (y!=a[i].length-1) System.out.print("\t");
            }
            System.out.print("|\t");
            System.out.print(b[i]);
            System.out.println();
        }

        for (int i = 0; i<n; i++){
            System.out.println("El valor de x"+(i+1)+" es: "+x[i]);
            System.out.printf("\tx%d = %.4f\t", i, x[i]);
        }
    }
}