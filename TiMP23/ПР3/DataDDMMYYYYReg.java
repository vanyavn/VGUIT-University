import java.util.regex.*;
public class DataDDMMYYYYReg {
    public static void main(String[] args) {
        String[] inputs = {"29/02/2000", "30/04/2003", "01/01/2003", "29/02/2001", "30-04-2003", "1/1/1899"};
        String regex = "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(16\\d{2}|[2-9]\\d{3})$";
        Pattern pattern = Pattern.compile(regex);
        for (String date : inputs) {
            Matcher matcher = pattern.matcher(date);
            if (matcher.matches()) {
                int year = Integer.parseInt(matcher.group(3));
                int month = Integer.parseInt(matcher.group(2));
                if (month == 2) {
                    if (year % 4 == 0) { System.out.printf("%s соответствует заданному формату даты.%n", date); }
                    else { System.out.printf("%s не соответствует заданному формату даты.%n", date); }
                } else { System.out.printf("%s соответствует заданному формату даты.%n", date); }
            } else { System.out.printf("%s не соответствует заданному формату даты.%n", date); }
        }
    }
}