import java.util.Arrays;
import java.util.Comparator;
public class Collections {
    private String Name;
    private int Year;
    public Collections(String Name, int Year) {
        this.Name=Name;
        this.Year=Year;
    }
    public String getName() { return Name; }
    public int getYear() { return Year; }
    public static void main(String[] args) {
        Collections[] collectionss= {new Collections("Преступление и Наказание ", 2011), new Collections("Мастер и Маргарита ", 1993), new Collections("Война и Мир ", 1997), new Collections("Король и Шут ", 2023)};
        System.out.println("\nИсходный массив:\n");
        for (Collections collections:collectionss) { System.out.println(collections.getName() +""+collections.getYear()); }
        System.out.println("\nСортировка по имени:\n");
        Arrays.sort(collectionss, Comparator.comparing(Collections::getName).thenComparing(Collections::getYear));
        for (Collections collections:collectionss) { System.out.println(collections.getName() +""+collections.getYear()); }
        System.out.println("\nСортировка по году издательства:\n");
        Arrays.sort(collectionss, Comparator.comparing(Collections::getYear).thenComparing(Collections::getName));
        for (Collections collections:collectionss) { System.out.println(collections.getName() +""+collections.getYear()); }      
    }
}