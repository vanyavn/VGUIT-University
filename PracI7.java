import java.util.Scanner;
import static java.lang.Math.*;
public class PracI7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите число x: ");
        double x = scanner.nextDouble();
        double y, f;
        if (x <= -3) {
            y = pow(x, 3) + 1;
            f = pow(E, (x + 1));
        } else if (x > 0) {
            y = pow((1 / tan(x)), 2);
            f = pow(tan(x), 1/5);
        } else {
            y = 1 + pow(2, tan(x));
            f = pow(x, 4);
        }
        System.out.println("Y = " + y);
        System.out.println("F = " + f);
        scanner.close();
    }
}