import java.util.Scanner;

public class Zadacha01 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array1 = new int[4];
        int[] array2 = new int[4];
        int[] array3 = new int[4];
        System.out.println("Введите элементы первого массива:");
        for (int i = 0; i < 4; i++) {
            array1[i] = scanner.nextInt();
        }
        System.out.println("Введите элементы второго массива:");
        for (int i = 0; i < 4; i++) {
            array2[i] = scanner.nextInt();
        }
        System.out.println("Введите элементы третьего массива:");
        for (int i = 0; i < 4; i++) {
            array3[i] = scanner.nextInt();
        }

        for (int i = 0; i < 4; i++) {
            int product = array1[i] * array2[i] * array3[i];
            System.out.println("Произведение " + (i+1) + "-го элемента: " + product);
        }
    }
}