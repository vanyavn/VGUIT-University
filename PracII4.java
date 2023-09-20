import java.util.Random;

public class PracII4 {
    public static void main(String[] args) {
        int n = 5; // размер матрицы
        int[][] A = new int[n][n]; // создаем матрицу n x n
        int minPositive = Integer.MAX_VALUE; // переменная для хранения минимального положительного элемента
        // заполняем матрицу случайными значениями от -10 до 10
        Random rnd = new Random();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = rnd.nextInt(19) - 9;
            }
        }
        // выводим матрицу на экран
        System.out.println("Матрица:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i][j] < 0) {
                        System.out.print(A[i][j]+"\t");
                }
                else {
                    System.out.print(A[i][j] + "\t");
                }
            }
            System.out.println();
        }
        // находим минимальный положительный элемент параллельно главной диагонали, расположенной выше диагонали
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (A[i][j] > 0 && A[i][j] < minPositive) {
                    minPositive = A[i][j];
                }
            }
        }
        // выводим результат на экран  
        if (minPositive == Integer.MAX_VALUE) {
            System.out.println("В матрице нет положительных элементов выше главной диагонали.");
        } else
        {
            System.out.println("Минимальный положительный элемент выше главной диагонали: " + minPositive);
        }
    }
}