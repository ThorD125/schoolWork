package classes;

public class CarFactory {
    private String brand;
    private int carsCount = 0;
    private String location;

    public CarFactory(String brandGiven, String LocationGiven) {
        this.brand = brandGiven;
        this.location = LocationGiven;
    }

    public Cars BuildCar() {

        java.util.Random r = new java.util.Random();
        int speed = 50 + r.nextInt(150);

        String[] colors = { "red", "green", "blue", "purple", "yellow", "orange", "pink", "hotpink", "darkblue",
                "black" };

        // java.util.Random r = new java.util.Random();
        int randcolor = 0 + r.nextInt(colors.length);
        String color = colors[randcolor];

        carsCount++;

        Cars createdCar = new Cars(brand, color, speed);
        return createdCar;
    }

    public String toString() {
        return brand + "-" + location + "(" + carsCount + ")";
    }
}
