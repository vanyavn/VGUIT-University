import java.io.*; import java.net.*; import java.util.zip.*; import java.nio.file.*;
public class TaskXXXIV {
    public static void main(String[] args) {
        try (Writer writer = new FileWriter("data1.txt")) {
            writer.write("");
            System.out.println("\nФайл data1 создан.");
        } catch (IOException e) { e.printStackTrace(); }
        try (Writer writer = new FileWriter("data2.txt")) {
            writer.write("");
            System.out.println("Файл data2 создан.");
        } catch (IOException e) { e.printStackTrace(); }
        try {
            String zipFile = "upload.zip";
            createZipArchive(zipFile, "data1.txt", "data2.txt");
            System.out.println("Архив успешно создан: " + zipFile);
            uploadToServer(zipFile, "http://example.com/upload");
        } catch (Exception e) {
            System.err.println("Ошибка: " + e.getMessage());
            e.printStackTrace();
        }
    }
    private static void createZipArchive(String zipFile, String... files) 
            throws IOException {
        try (ZipOutputStream zos = new ZipOutputStream(
             new FileOutputStream(zipFile))) {
            for (String file : files) {
                // Добавляем проверку существования файла
                if (!Files.exists(Paths.get(file))) {
                    System.err.println("Файл " + file + " не найден!");
                    continue;
                }  
                try (FileInputStream fis = new FileInputStream(file)) {
                    ZipEntry zipEntry = new ZipEntry(file);
                    zos.putNextEntry(zipEntry); 
                    byte[] buffer = new byte[1024];
                    int length;
                    while ((length = fis.read(buffer)) > 0) {
                        zos.write(buffer, 0, length);
                    }
                    zos.closeEntry();
                    System.out.println("Файл " + file + " добавлен в архив");
                }
            }
        }
    }
    private static void uploadToServer(String filePath, String url) 
            throws IOException {
        HttpURLConnection connection = (HttpURLConnection) 
            new URL(url).openConnection();
        connection.setDoOutput(true);
        connection.setRequestMethod("POST");

        try (OutputStream os = connection.getOutputStream();
             FileInputStream fis = new FileInputStream(filePath)) {
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                os.write(buffer, 0, bytesRead);
            }
        }
        int responseCode = connection.getResponseCode();
        System.out.println("Ответ сервера: " + responseCode);
    }
}