import java.util.Scanner;
public class PracI2 {
   
    public static void main(String[] args) {
           
        Scanner in = new Scanner(System.in);
        System.out.print("Введите Ваше количество параметров: ");
        String num = in.nextLine();
        if (num.length() > 0){
            System.out.printf("Вы ввели %s параметров\n", num);
        }
        else {
            System.out.println("Вы не передавали параметров");
        }   
        in.close();
    }
}