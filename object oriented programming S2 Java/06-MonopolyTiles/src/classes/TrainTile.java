package classes;

public class TrainTile extends Tile {
    private int rent;
    private int cost;
    private int mortgage;

    public TrainTile(int position, String name, int rent, int cost, int mortgage) {
        super(position, name, "Train");
        this.rent = rent;
        this.cost = cost;
        this.mortgage = mortgage;
    }

    public int getRent() {
        return rent;
    }

    public int getCost() {
        return cost;
    }

    public int getMortgage() {
        return mortgage;
    }

    public String toString() {
        return super.toString() + "Rent: " + rent + ", Cost: " + cost + ", Mortgage: " + mortgage;
    }

}
