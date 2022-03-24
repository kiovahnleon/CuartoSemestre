public class gaussv1{

    public static void main(String[] args) {
        double x [][]={{2.0,1.0,-3.0,-1.0},
                        {-1.0,3.0,2.0,12.0},
                        {3.0,1.0,-3.0,0.0}};
        double solution[] = new double[x.length];

        int n = x.length;

        for(int col=0;col<n-1;col++){
            for(int i=1+col;1<n;i++){
                double multiplica = x[i][col]/x[col][col];
                for(int j = 0+col;j<n+1;j++){
                    x[i][j] = x[i][j]-(multiplica)*(x[col][j]);
                }
            }
        }

        solution[n-1] = (x[n-1][n])/x[n-1][n-1];

        for (int i=n-2; i>0 ; i--){
            double sumatoria = 0;
            for(int j = i; j < n; j++){
                sumatoria += (x[i][j]*solution[j]);
            }
            solution[i]=(x[i][n]-sumatoria)/x[i][i];
        }
        System.out.println("Matriz Escalonada");
        imprimirMatriz(x);
        System.out.println("Vactor de resultados");
        imprimirVector(solution);
    }
}

