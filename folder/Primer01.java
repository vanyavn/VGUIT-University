import java.util.Scanner;

public class Primer01 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Введите размерность матрицы: ");
        int n = sc.nextInt();
        int[][] A = new int[n][n]; // создание двумерного массива
        int sumMainDiagonal = 0; // переменная для хранения суммы элементов главной диагонали
        int sumSecondaryDiagonal = 0; // переменная для хранения суммы элементов побочной диагонали
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = (int) (Math.random() * 100); // случайное число от 0 до 99
            }
        }
        for (int i = 0; i < n; i++) {
            sumMainDiagonal += A[i][i];
        }
        for (int i = 0; i < n; i++) {
            sumSecondaryDiagonal += A[i][n - i - 1];
        }
        System.out.println("Матрица:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Сумма элементов главной диагонали: " + sumMainDiagonal);
        System.out.println("Сумма элементов побочной диагонали: " + sumSecondaryDiagonal);
    }
}