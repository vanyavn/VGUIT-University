import java.util.Arrays;

public class MatrixDeterminantDemo {
    public static void main(String[] args) {
        int[][] matrix = {
            {2, -3, 1},
            {4, 0, -2},
            {3, -1, 5}
        };
        
        System.out.println("\nМатрица:");
        printMatrix(matrix);
        
        int determinant = calculateDeterminant(matrix);
        System.out.println("\nОпределитель матрицы: " + determinant);
    }
    
    private static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
    
    private static int calculateDeterminant(int[][] matrix) {
        if (matrix.length == 2) {
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
        }
        
        int determinant = 0;
        for (int i = 0; i < matrix.length; i++) {
            int[][] minor = new int[matrix.length - 1][matrix.length - 1];
            for (int j = 1; j < matrix.length; j++) {
                for (int k = 0, l = 0; k < matrix.length; k++) {
                    if (k != i) {
                        minor[j - 1][l++] = matrix[j][k];
                    }
                }
            }
            determinant += (i % 2 == 0 ? 1 : -1) * matrix[0][i] * calculateDeterminant(minor);
        }
        return determinant;
    }
}