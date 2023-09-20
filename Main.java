import java.util.ArrayList;
import java.util.Scanner;
class Stroymaterialy {
    protected String name;
    public Stroymaterialy(String name) { this.name = name; }
    public String getName() { return name; }
}
class Cement extends Stroymaterialy { public Cement(String name) { super(name); } }
class Brick extends Stroymaterialy { public Brick(String name) { super(name); } }
public class Main {
    private static ArrayList<Stroymaterialy> stroymaterialyList = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        boolean exit = false;
        while (!exit) {
            System.out.println("- - Меню - -:");
            System.out.println("1. Добавить стройматериал");
            System.out.println("2. Вывести все стройматериалы");
            System.out.println("3. Выход");
            System.out.print("Выберите пункт меню: ");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    addStroymaterial();
                    break;
                case 2:
                    printStroymaterialy();
                    break;
                case 3:
                    System.out.println("Вы вышли");
                    exit = true;
                    break;
                default:
                    System.out.println("Неверный выбор");
            }
            System.out.println();
        }
    }
    private static void addStroymaterial() {
        System.out.println("Выберите тип стройматериала:");
        System.out.println("1. Цемент");
        System.out.println("2. Кирпич");
        System.out.print("Введите выбранный тип: ");
        int typeChoice = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Введите название: ");
        String name = scanner.nextLine();
        switch (typeChoice) {
            case 1:
                stroymaterialyList.add(new Cement(name));
                break;
            case 2:
                stroymaterialyList.add(new Brick(name));
                break;
            default: System.out.println("Неверный выбор типа стройматериала.");
        }
    }
    private static void printStroymaterialy() {
        if (stroymaterialyList.isEmpty()) {
            System.out.println("Стройматериалы не добавлены.");
            return;
        }
        System.out.println("Список стройматериалов:");
        for (Stroymaterialy stroymaterial : stroymaterialyList) {
            System.out.println("Тип: " + stroymaterial.getClass().getSimpleName());
            System.out.println("Название: " + stroymaterial.getName());
            System.out.println("- - - - -");
        }
    }
}