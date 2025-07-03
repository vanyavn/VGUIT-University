import java.util.HashSet;
public class TaskIV {
    public static void main(String[] args) {
        HashSet<String> fruits = new HashSet<>();
        fruits.add("яблоко");
        fruits.add("груша");
        fruits.add("яблоко");
        fruits.add("апельсин");
        System.out.println("\nУникальные элементы: " + fruits);
    }
}