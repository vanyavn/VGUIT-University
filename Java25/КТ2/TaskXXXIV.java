import java.util.*;
import java.util.stream.Collectors;
class Product {
    String category;
    String name;
    Product(String category, String name) {
        this.category = category;
        this.name = name;
    }
}
public class TaskXXXIV {
    public static void main(String[] args) {
        List<Product> inventory = List.of(
            new Product("Электроника", "Телевизор"),
            new Product("Электроника", "Телефон"),
            new Product("Еда", "Колбаса"),
            new Product("Электроника", "Компьютер"),
            new Product("Еда", "Молоко"),
            new Product("Одежда", "Спортивный костюм")
        );
        Map<String, List<Product>> groupedProducts = inventory.stream()
            .collect(Collectors.groupingBy(product -> product.category));
        System.out.println("\n\nТовары по категориям:");
        groupedProducts.forEach((category, products) -> 
            System.out.println(category + ": " + 
                products.stream()
                    .map(p -> p.name)
                    .collect(Collectors.toList())));
    }
}