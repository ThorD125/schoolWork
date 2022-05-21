package classes;

public class Cars {
    private String brand;// = "Volvo";
    private String color;// = "#FFFFFF";
    private int maxspeed;// = 500;

    public Cars(String brandGiven, String colorGiven, int maxspeedGiven) {
        brand = brandGiven;
        color = colorGiven;
        maxspeed = maxspeedGiven;
    }

    public String getColor() {
        return color;
    }

    public String toString() {
        return color + " " + brand + "(" + maxspeed + ")";
    }

    public void repaint(String newColor) {
        color = newColor;
    }
}
