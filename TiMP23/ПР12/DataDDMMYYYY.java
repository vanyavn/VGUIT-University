import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
public class DataDDMMYYYY {
    public static void main(String[] args) {
        String[] inputs = {"29/02/2000", "30/04/2003", "01/01/2003", "29/02/2001", "30-04-2003", "1/1/1899"};
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        dateFormat.setLenient(false);
        for (String input : inputs) {
            try {
                if (isValidDate(input, dateFormat)) { System.out.println(input + " соответствует заданному формату даты.");
                } else { throw new ParseException("Неверный формат даты.", 0); }
            } catch (ParseException e) { System.out.println(input + " не соответствует заданному формату даты."); }
        }
    }
    public static boolean isValidDate(String dateStr, SimpleDateFormat dateFormat) {
        try {
            Date date = dateFormat.parse(dateStr);
            String formattedDate = dateFormat.format(date);
            return dateStr.equals(formattedDate);
        } catch (ParseException e) { return false; }
    }
}