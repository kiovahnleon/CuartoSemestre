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
                    x[i]
                }
            }
        }
    }
}

