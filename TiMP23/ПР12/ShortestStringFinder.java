import java.util.Scanner;
class ShortestStringFinder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите количество строк (n): ");
        int n = scanner.nextInt();
        scanner.nextLine();
        String shortestString = null;
        int shortestLength = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            System.out.print("Введите строку №" + (i + 1) + ": ");
            String input = scanner.nextLine();   
            if (input.length() < shortestLength) {
                shortestString = input;
                shortestLength = input.length();
            }
        }
        if (shortestString != null) {
            System.out.println("Самая короткая строка: " + shortestString);
            System.out.println("Длина: " + shortestLength);
        } else { System.out.println("Вы не ввели ни одной строки."); }
        scanner.close();
    }
}