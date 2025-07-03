class Car {
  String model; double weight; double speed;
  public Car(String model, double weight, double speed) {
    this.model = model;
    this.weight = weight;
    this.speed = speed;
  }
  public void displayInfo() {
    System.out.println("Модель: " + model);
    System.out.println("Вес: " + weight + " кг");
    System.out.println("Скорость: " + speed + " км/ч");
  }
  public double calculateTotalRentCost(int hours) { return calculateRentCost(hours) + calculateFuelCost(hours); }
  public double calculateRentCost(int hours) { return 0.0; }
  public double calculateFuelCost(int hours) { return 0.0; }
}
class BentleyTurboR extends Car {
  public BentleyTurboR() { super("BentleyTurboR", 1500, 180); }
  @Override
  public double calculateRentCost(int hours) { return 250 * hours; }
  @Override
  public double calculateFuelCost(int hours) {
    double fuelConsumption = (9.0 / 100.0) * (speed * hours);
    double fuelCost = fuelConsumption * 50.0;
    return fuelCost;
  }
}
class Truck extends Car {
  double loadCapacity; double loadWeight;
  public Truck(String model, double weight, double speed, double loadCapacity, double loadWeight) {
    super(model, weight, speed);
    this.loadCapacity = loadCapacity;
    this.loadWeight = loadWeight;
  }
  @Override
  public double calculateRentCost(int hours) {
    return loadWeight * 10 * hours;
  }
  @Override
  public double calculateFuelCost(int hours) {
    return (loadWeight / 100) * 10 * hours;
  }
}
class Bus extends Car {
  int capacity;
  double comfortCoefficient;
  public Bus(String model, double weight, double speed, int capacity, double comfortCoefficient) {
    super(model, weight, speed);
    this.capacity = capacity;
    this.comfortCoefficient = comfortCoefficient;
  }
  @Override
  public double calculateRentCost(int hours) { return capacity * 15 * comfortCoefficient * hours; }
  @Override
  public double calculateFuelCost(int hours) {
    double distance = speed * hours;
    return (distance / 50) * 10;
  }
}
class Fleet {
  Car[] cars;
  public Fleet(Car[] cars) { this.cars = cars; }
  public Car findCarByModel(String model) {
    for (Car car : cars) { if (car.model.equals(model)) { return car; } }
    return null;
  }
  public Car findFastestBus() {
    Bus fastestBus = null;
    double maxSpeed = 0;
    for (Car car : cars) {
      if (car instanceof Bus && car.speed > maxSpeed) {
        maxSpeed = car.speed;
        fastestBus = (Bus) car;
      }
    }
    return fastestBus;
  }
}
public class pr4 {
  public static void main(String[] args) {
    Car car1 = new Truck("Грузовик 1", 2000, 100, 5, 1000);
    Car car2 = new Bus("Автобус 1", 1500, 80, 40, 1.2);
    Car car3 = new Bus("Автобус 2", 1600, 90, 50, 1.3);
    Car car4 = new BentleyTurboR();
    Car[] cars = { car1, car2, car3, car4 };
    Fleet fleet = new Fleet(cars);
    Car cheapestCar = fleet.findCarByModel("Bus2");
    if (cheapestCar != null) {
      System.out.println("Самый медленный автомобиль:");
      cheapestCar.displayInfo();
      System.out.println("Total rent cost: " + cheapestCar.calculateTotalRentCost(3));
    }
    Bus fastestBus = (Bus) fleet.findFastestBus();
    if (fastestBus != null) {
      System.out.println("Самый быстрый автобус:");
      fastestBus.displayInfo();
    }
    System.out.println("Информация о Bentley Turbo R:");
    car4.displayInfo();
    int hours = 3;
    double rentCost = car4.calculateRentCost(hours);
    double fuelCost = car4.calculateFuelCost(hours);
    double totalCost = rentCost + fuelCost;
    System.out.println("BentleyTurboR");
    System.out.println("Стоимость аренды: " + rentCost);
    System.out.println("Стоимость топлива: " + fuelCost);
    System.out.println("Итоговая стоимсоть: " + totalCost);
  }
}