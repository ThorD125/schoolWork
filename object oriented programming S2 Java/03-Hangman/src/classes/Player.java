package classes;

public class Player {
    private int wins;
    private String name;

    public Player(String name) {
        this.name = name;
        this.wins = 0;
    }

    public String toString() {
        return this.name + " has " + this.wins + " wins.";
    }

    public void addWin() {
        this.wins++;
    }

    public int getWins() {
        return this.wins;
    }

    public String getName() {
        return this.name;
    }
}
