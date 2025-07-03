import java.util.regex.*;
public class Abcdefg {
    public static void main(String[] args) {
        String inp1 = "abcdefghijklmnopqrstuv18340";
        String inp2 = "abcdefghijklmnoasdfasdpqrstuv18340";
        String reg = "^abcdefghijklmnopqrstuv18340$";
        boolean ism1 = Pattern.matches(reg, inp1);
        boolean ism2 = Pattern.matches(reg, inp2);
        if (ism1) { System.out.printf("Строка %s соответствует заданному шаблону.\n", inp1); }
        else { System.out.printf("Строка %s не соответствует заданному шаблону.\n", inp1); }
        if (ism2) { System.out.printf("Строка %s соответствует заданному шаблону.\n", inp2); }
        else { System.out.printf("Строка %s не соответствует заданному шаблону.\n", inp2); }
    }
}