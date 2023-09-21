import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;
public class LiteratureManagement {
    private static ArrayList<Book> books = new ArrayList<>();
    private static final String FILE_PATH = "books.txt";
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\n----- Меню учёта литературы -----\n" +
                    "1. Добавить книгу\n" +
                    "2. Вывести список книг\n" +
                    "3. Отсортировать список\n" +
                    "4. Сохранить список в файл\n" +
                    "5. Загрузить список из файла\n" +
                    "6. Выйти");

            System.out.print("Введите свой выбор: ");
            choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.println("\nДобавить книгу:");
                    System.out.print("Название: ");
                    String title = sc.nextLine();
                    System.out.print("Автор: ");
                    String author = sc.nextLine();
                    System.out.print("Издательство: ");
                    String publisher = sc.nextLine();
                    System.out.print("Год издательства: ");
                    int publicationYear = sc.nextInt();
                    System.out.print("Цена: ");
                    double basePrice = sc.nextDouble();
                    System.out.print("Количество страниц: ");
                    int numPages = sc.nextInt();
                    Book book = new Book(title, author, publisher, publicationYear, basePrice, numPages);
                    books.add(book);
                    System.out.println("Книга успешно добавлена!");
                    break;
                case 2:
                    System.out.println("\nСписок книг:");
                    displayBooks();
                    break;
                case 3:
                    System.out.println("\nОтсортированный список книг:");
                    sortBooksByTitle();
                    displayBooks();
                    break;
                case 4:
                    saveBooksToFile();
                    break;
                case 5:
                    loadBooksFromFile();
                    break;
                case 6:
                    System.out.println("\nВы вышли из меню учёта литературы!");
                    break;
                default:
                    System.out.println("Неверный выбор! Попробуйте ещё раз.");
                    break;
            }
        } while (choice != 6);
    }
    private static void sortBooksByTitle() { Collections.sort(books, Comparator.comparing(Book::getTitle)); }
    private static void displayBooks() {
        if (books.isEmpty()) { System.out.println("Список книг пуст!"); }
        else { for (Book book : books) { System.out.println(book); } }
    }
    private static void saveBooksToFile() {
        try (PrintWriter writer = new PrintWriter(new FileWriter(FILE_PATH))) {
            for (Book book : books) {
                writer.println(book.getTitle() + ";" +
                        book.getAuthor() + ";" +
                        book.getPublisher() + ";" +
                        book.getPublicationYear() + ";" +
                        book.getBasePrice() + ";" +
                        book.getNumPages());
            }
            System.out.println("Список книг успешно сохранён в файл!");
        } catch (IOException e) {
            System.out.println("Ошибка при сохранении списка книг в файл!");
            e.printStackTrace(); //
        }
    }
    private static void loadBooksFromFile() {
        books.clear(); // Очищаем текущий список книг перед загрузкой из файла
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] data = line.split(";");
                String title = data[0];
                String author = data[1];
                String publisher = data[2];
                int publicationYear = Integer.parseInt(data[3]);
                double basePrice = Double.parseDouble(data[4]);
                int numPages = Integer.parseInt(data[5]);
                Book book = new Book(title, author, publisher, publicationYear, basePrice, numPages);
                books.add(book);
            }
            System.out.println("Список книг успешно загружен из файла!");
        } catch (IOException e) {
            System.out.println("Ошибка при загрузке списка книг из файла!");
            e.printStackTrace();
        }
    }
    static class Book {
        private String title;
        private String author;
        private String publisher;
        private int publicationYear;
        private double basePrice;
        private int numPages;
        public Book(String title, String author, String publisher, int publicationYear, double basePrice, int numPages) {
            this.title = title;
            this.author = author;
            this.publisher = publisher;
            this.publicationYear = publicationYear;
            this.basePrice = basePrice;
            this.numPages = numPages;
        }
        public String getTitle() { return title; }
        public String getAuthor() { return author; }
        public String getPublisher() { return publisher; }
        public int getPublicationYear() { return publicationYear; }
        public double getBasePrice() { return basePrice; }
        public int getNumPages() { return numPages; }
        @Override
        public String toString() {
            return "Книга: " + title + "\n" +
                    "Автор: " + author + "\n" +
                    "Издательство: " + publisher + "\n" +
                    "Год издательства: " + publicationYear + "\n" +
                    "Цена: " + basePrice + "\n" +
                    "Количество страниц: " + numPages + "\n";
        }
    }
}