import java.util.Arrays;

public class ArrayReverseDemo {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        System.out.println("Исходный массив: " + Arrays.toString(array));
        
        for (int i = 0; i < array.length / 2; i++) {
            int temp = array[i];
            array[i] = array[array.length - 1 - i];
            array[array.length - 1 - i] = temp;
        }
        
        System.out.println("Массив после обращения: " + Arrays.toString(array));
    }
}