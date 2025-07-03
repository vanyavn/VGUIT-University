import java.util.ArrayList;
import java.util.List;
public class TaskXIV {
    public static void main(String[] args) {
        List<Integer> firstNumbers = new ArrayList<>(List.of(1, 2, 3, 4));
        List<Integer> secondNumbers = new ArrayList<>(List.of(3, 4, 5, 6));
        System.out.println("\nПервая коллекция: " + firstNumbers + "\nВторая коллекция: " + secondNumbers);
        firstNumbers.retainAll(secondNumbers);
        System.out.println("\nОбщие элементы: " + firstNumbers);
    }
}