import java.io.*;
public class TaskXIV {
    public static void main(String[] args) {
        try (Writer writer = new FileWriter("output.txt")) {
            writer.write("Пример текста для записи в файл\n");
            writer.write("Вторая строка данных");
        } catch (IOException e) { e.printStackTrace(); }
    }
}