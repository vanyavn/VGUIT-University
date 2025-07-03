import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class TaskXXIV {
    public static void main(String[] args) {
        List<String> letters = new ArrayList<>(List.of("A", "B", "C"));
        String[] lettersArray = letters.toArray(new String[0]);
        System.out.println("\nПреобразованный массив: " + Arrays.toString(lettersArray));
    }
}