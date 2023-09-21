import java.util.Scanner;

public class Zadacha {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] a = new int[4];
        int[] b = new int[4];
        int[] c = new int[4];
        System.out.println("Введите элементы первого массива:");
        for (int i = 0; i < 4; i++) {
            a[i] = scanner.nextInt();
            b[i] = scanner.nextInt();
            c[i] = scanner.nextInt();
        }

        for (int i = 0; i < 4; i++) {
            int product = a[i] * b[i] * c[i];
            System.out.println("Произведение " + (i+1) + "-го элемента: " + product);
        }
    }
}