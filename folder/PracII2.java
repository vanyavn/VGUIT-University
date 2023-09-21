import java.util.Arrays;

public class PracII2 {
    public static void main(String[] args) {
        double[] b = {-10, 12.5, 30.4, 20, 0};
        for (int i = 0; i < b.length; i++) {
            b[i] = Math.round(b[i] * 100.0) / 100.0;
        }
        double[] c = new double[b.length];
        System.out.printf("Исходный массив:\n\n%s", Arrays.toString(b));
        System.out.println();
        int index = 0;
        for (double num : b) {
            if (num > 0) {
                c[index] = Math.sqrt(num);
                index++;
            }
        }
        c = Arrays.copyOf(c, index);
        for (int i = 0; i < c.length; i++) {
            c[i] = Math.round(c[i] * 100.0) / 100.0;
        }
        selectionSort(c);
        System.out.printf("\nПолученный массив:\n\n%s", Arrays.toString(c));
        System.out.println();
    }
    public static void selectionSort(double[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                double temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }
}