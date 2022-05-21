package classes;

public class Tile {
    private final int position;
    private final String name;

    private String Type;


    public Tile(int position, String name, String type) {
        this.position = position;
        this.name = name;
        this.Type = type;
    }

    public int getPosition() {
        return position;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return Type;
    }

    public String toString() {
        return "Tile " + name + " (" + position + ")";
    }

}