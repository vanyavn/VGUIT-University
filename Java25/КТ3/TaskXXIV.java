import java.io.*;
import java.util.zip.*;
import java.nio.file.*;

public class TaskXXIV {
    public static void main(String[] args) {
        try (Writer writer = new FileWriter("file1.txt")) {
            writer.write("");
            System.out.println("\nФайл file1 создан.");
        } catch (IOException e) { e.printStackTrace(); }
        try (Writer writer = new FileWriter("file2.txt")) {
            writer.write("");
            System.out.println("\nФайл file2 создан.");
        } catch (IOException e) { e.printStackTrace(); }
        try (ZipOutputStream zos = new ZipOutputStream(new FileOutputStream("archive.zip"))) {
            addToZip(zos, "file1.txt");
            addToZip(zos, "file2.txt");
        } catch (IOException e) {
            System.err.println("\nОшибка при создании архива: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static void addToZip(ZipOutputStream zos, String filename) {
        Path filePath = Paths.get(filename);
        if (!Files.exists(filePath)) {
            System.err.println("\nФайл не найден: " + filename);
            return;
        }

        try {
            ZipEntry entry = new ZipEntry(filePath.getFileName().toString());
            zos.putNextEntry(entry);
            Files.copy(filePath, zos);
            zos.closeEntry();
            System.out.println("\nДобавлен файл: " + filename);
        } catch (IOException e) {
            System.err.println("\nНе удалось добавить файл: " + filename);
            e.printStackTrace();
        }
    }
}
