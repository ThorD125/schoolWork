package classes;

public class CreatePlayers {

    private final IO io = new IO();

    public CreatePlayers() {
        Player player1;
        Player player2;


    String name = io.promptForText("What is your name player1?");

    boolean correct = io.promptForBoolean("Is " + name + " your real name player1?");

    if(correct)
    {
        io.show("The I will call you " + name);
        player1 = new Player(name);
    }else
    {
        io.show("The I will call you liar.");
        player1 = new Player("liar");
    }

    name=io.promptForText("What is your name player2?");

    correct=io.promptForBoolean("Is "+name+" your real name player2?");

    if(correct)
    {
        io.show("The I will call you " + name);
        player2 = new Player(name);
    }else
    {
        io.show("The I will call you liar.");
        player2 = new Player("liar");
    }

    if(player1.getName().equals(player2.getName()))
    {
        io.show("You both are named " + player1.getName() + ". Let's play!");
    }else
    {
        io.show("Let's play!");
    };

    Hangman.PlayGame(player1, player2);
    }
;