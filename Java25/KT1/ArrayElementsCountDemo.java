import java.util.Arrays;
public class ArrayElementsCountDemo {
    public static void main(String[] args) {
        int[] array = {3, -2, 0, 5, -1, 0, 7, 0, -4};
        System.out.println("\nМассив: " + Arrays.toString(array));
        
        int positive = 0, negative = 0, zero = 0;
        for (int num : array) {
            if (num > 0) positive++;
            else if (num < 0) negative++;
            else zero++;
        }
        System.out.println("Положительных элементов: " + positive);
        System.out.println("Отрицательных элементов: " + negative);
        System.out.println("Нулевых элементов: " + zero);
    }
}