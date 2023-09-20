import java.util.Scanner;
public class PracI3 {
    public static void main (String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("Введите а : ");
        String a = in.nextLine();
        System.out.println("Введите b : ");
        String b = in.nextLine();
        if (a.length() == 0){
            System.out.println("Неверное количество параметров");
        }
        if (b.length() == 0){
            System.out.println("Неверное количество параметров");
        }
        else{
            int aa = Integer.parseInt(a);
            int bb = Integer.parseInt(b);
            System.out.printf("Вы ввели a равное %d \n", aa);
            System.out.printf("Вы ввели b равное %d \n", bb);
            System.out.printf("Сумма a и b равна %d \n", aa+bb);
        }   
        in.close();
    }
}
        