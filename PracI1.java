import java.util.Scanner;

public class PracI1 {
   
    public static void main(String[] args) {
           
        Scanner in = new Scanner(System.in);
        System.out.print("Введите имя: ");
        String name = in.nextLine();
        if (name.length() != 0){
            System.out.printf("Hello, %s \n", name);
        }
        else{
            System.out.println("Hello world");
        }   
        in.close();
    }
}