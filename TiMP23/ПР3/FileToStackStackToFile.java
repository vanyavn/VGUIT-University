import java.io.*; import java.util.Stack;
public class FileToStackStackToFile {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) { stack.push(line); }
            while (!stack.isEmpty()) { writer.write(stack.pop() + "\n"); }
            System.out.println("Операция прошла успешно!");
        } catch (IOException e) {
            System.out.println("Ошибка! Скорее всего файл input не создан.");
            e.printStackTrace();
        } } }