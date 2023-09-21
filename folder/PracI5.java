import java.util.Scanner;
public class PracI5 {
    public static void main (String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("Введите x : ");
        int x = in.nextInt();
        System.out.println("Введите y : ");
        int y = in.nextInt();
        if (x < y) {
            System.out.println("Результат");
            System.out.println(x / 2);
        }

        else {
            System.out.println("Результат");
            System.out.println(y / 2);
        }   
        in.close();
    }
}