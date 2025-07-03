import java.nio.file.*;
public class TaskIV {
    public static void main(String[] args) throws Exception {
        Path newDir = Paths.get("new_directory");
        Files.createDirectory(newDir);
        System.out.println("\nДиректория создана: " + newDir.toAbsolutePath());
    }
}