public class TextCleaner {
    public static void main(String[] args) {
        String inputText = "ツ Я люблю учиться! ツ";
        String cleanedText = inputText.replaceAll("[^А-Яа-яA-Za-z ]+", "").replaceFirst(" ", "-").replaceAll(" ", "").replaceAll("-"," ");
        System.out.println("Исходный текст:"+inputText);
        System.out.println("Результат:"+cleanedText);
    }
}