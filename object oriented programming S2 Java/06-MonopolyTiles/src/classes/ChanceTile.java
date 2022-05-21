package classes;

public class ChanceTile extends Tile {
    boolean isChance = true; // if false then iets community chest

    public ChanceTile(int position, String name, boolean isChance) {
        super(position, name, getType(isChance));
        this.isChance = isChance;
    }

    static public String getType(boolean isChance) {
        if (isChance) {
            return "chance";
        } else {
            return "community chest";
        }
    }


    public String toString() {
        if (isChance) {
            return "Chance" + super.toString();
        } else  {
            return "Community Chest" + super.toString();
        }
    }
}
