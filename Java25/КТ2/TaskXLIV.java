import java.util.*;

class EmptyCollectionException extends Exception {
    public EmptyCollectionException(String message) {
        super(message);
    }
}

public class TaskXLIV {
    public static void main(String[] args) {
        List<Integer> data = new ArrayList<>();
        
        try {
            validateCollection(data);
        } catch (EmptyCollectionException e) {
            System.out.println("\nПроверка не пройдена: " + e.getMessage());
        }
    }
    
    public static void validateCollection(Collection<?> collection) 
            throws EmptyCollectionException {
        if (collection.isEmpty()) {
            throw new EmptyCollectionException("Коллекция не должна быть пустой!");
        }
    }
}