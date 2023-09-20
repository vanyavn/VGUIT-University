import java.util.Scanner;
import static java.lang.Math.*;
public class PracI6 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Введите число a: ");
        double a = in.nextDouble();
        System.out.print("Введите число b: ");
        double b = in.nextDouble();
        double cosMax = cos(max(a, b));
        System.out.println("Косинус максимального числа: " + cosMax);
        in.close();
    }
}