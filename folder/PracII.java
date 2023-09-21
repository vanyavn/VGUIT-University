import java.util.Random;

public class PracII {
    
    public static int[] fillRandomIntVector(int size, int min, int max) {
        int[] vector = new int[size];
        Random rand = new Random();
        for (int i = 0; i < size; i++) {
            vector[i] = rand.nextInt((max - min) + 1) + min;
        }
        return vector;
    }
    
    public static void printVector(int[] vector, String message) {
        System.out.println(message);
        for (int i = 0; i < vector.length; i++) {
            System.out.print(vector[i] + " ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        int[] result = fillRandomIntVector(10, 0, 100);
        System.out.println();
        printVector(result, "Sorted vector:");
    }
}