public class ShapeDemo {
    public static void main(String[] args) {
        Shape circle = new Circle(5);
        Shape rectangle = new Rectangle(4, 6);
        
        circle.printInfo();
        rectangle.printInfo();
    }
}

abstract class Shape { public abstract void printInfo(); }
class Circle extends Shape {
    private double radius;
    public Circle(double radius) { this.radius = radius; }
    @Override
    public void printInfo() {
        System.out.println("\nКруг с радиусом " + radius + 
                         ", площадь: " + (Math.PI * radius * radius));
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }    
    @Override
    public void printInfo() {
        System.out.println("Прямоугольник " + width + "x" + height + 
                         ", площадь: " + (width * height));
    }
}