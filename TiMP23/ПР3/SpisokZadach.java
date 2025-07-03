import java.util.ArrayList; import java.util.List; import java.util.Scanner;
class Task {
    private String description;
    public Task(String description) { this.description = description; }
    public String getDescription() { return description; }
}
public class SpisokZadach {
    public static void main(String[] args) {
        List<Task> tasks = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Добавить задачу");
            System.out.println("2. Удалить задачу");
            System.out.println("3. Просмотреть задачи");
            System.out.println("4. Выход");
            System.out.print("Выберите действие: ");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Введите описание задачи: ");
                    scanner.nextLine();
                    String description = scanner.nextLine();
                    Task task = new Task(description);
                    tasks.add(task);
                    break;
                case 2:
                    System.out.print("Введите номер задачи для удаления: ");
                    int index = scanner.nextInt();
                    if (index >= 0 && index < tasks.size()) {
                        tasks.remove(index);
                    } else {
                        System.out.println("Неверный номер задачи.");
                    }
                    break;
                case 3:
                    System.out.println("Список задач:");
                    boolean pust = tasks.isEmpty();
                    if (pust == true) { System.out.println("Список задач пуст!"); } else {
                    for (int i = 0; i < tasks.size(); i++) {
                        Task t = tasks.get(i);
                        System.out.println(i + ". " + t.getDescription());
                    } }
                    break;
                case 4:
                    System.out.println("Выход из приложения.");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Неверный выбор.");
            }
        }
    }
}