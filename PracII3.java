import java.util.Random;

public class PracII3 {
    public static void main(String[] args) {
        int[][] matrix = new int[5][5]; // создаем матрицу 5x5
        Random random = new Random(); // создаем объект для генерации случайных чисел
        int[] b = new int[5]; // создаем вектор для хранения количества четных чисел в каждой строке

        // заполняем матрицу случайными значениями от 0 до 9
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = random.nextInt(10);
            }
        }

        // вычисляем количество четных чисел в каждой строке и записываем в вектор b
        for (int i = 0; i < matrix.length; i++) {
            int count = 0;
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] % 2 == 0) {
                    count++;
                }
            }
            b[i] = count;
        }

        // выводим матрицу и вектор на экран
        System.out.println("Матрица:");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Вектор B:");
        for (int i = 0; i < b.length; i++) {
            System.out.print(b[i] + " ");
        }
    }
}