import java.util.ArrayList;
import java.util.Arrays;

public class PracII1 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 4, 5, 3, 0, 0, 0, 2, 4}; // исходный массив
        ArrayList<Integer> duplicates = new ArrayList<>(); // создаем пустой список для повторяющихся элементов
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j] && !duplicates.contains(arr[i])) { // если найден повторяющийся элемент и его еще нет в списке
                    duplicates.add(arr[i]); // добавляем его в список
                }
            }
        }
        System.out.println("Исходный массив: " + Arrays.toString(arr));
        System.out.println("Массив-дубликаты: " + Arrays.toString(duplicates.toArray())); // выводим список повторяющихся элементов на экран
    }
}