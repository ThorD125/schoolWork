package classes;

public class StreetTile extends Tile {

    private int color;

    private int cost;
    private int mortgage;

    private int rent;

    private int houseCost;
    private int hotelCost;

    public StreetTile(int position, String name, int color, int rent, int houseCost, int hotelCost) {
        super(position, name, "Street");
        this.color = color;
        this.rent = rent;

        this.houseCost = houseCost;
        this.hotelCost = hotelCost;
    }

    public String toString() {
        return color + super.toString() + cost;
    }

    public void setColor(int color) {
        this.color = color;
    }

    public int getCost() {
        return cost;
    }

    public int getMortgage() {
        return mortgage;
    }

    public int getRent() {
        return rent;
    }

    public int getHouseCost() {
        return houseCost;
    }

    public int getColor() {
        return color;
    }

    public int getHotelCost() {
        return hotelCost;
    }
}
