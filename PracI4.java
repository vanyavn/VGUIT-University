import java.util.Scanner;
public class PracI4 {
    public static void main (String[] args){
        String password = "uytrewq";
        String login = "vanyok";
        Scanner in = new Scanner(System.in);
        System.out.println("Введите логин : ");
        String a = in.nextLine();
        System.out.println("Введите пароль : ");
        String b = in.nextLine();
        if ((a.equals(login))&&(b.equals(password))){
            System.out.println("Вас узнали. Добро пожаловать");
        }
        else{
            System.out.println("Логин и пароль не распознаны. Доступ запрещен");
        }   
        in.close();
    }
}
        