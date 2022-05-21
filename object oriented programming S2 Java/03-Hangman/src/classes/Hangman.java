package classes;

public class Hangman {

    public static void main(String[] args) {
        new Hangman().start();
    }

    private final IO io = new IO();

    private void start() {
        io.show("Welcome to Hangman");
        boolean correct = io.promptForBoolean("Do you have a friend to play this little game?");

        if (correct) {
            io.show("Great! Let's play!");
            new CreatePlayers();
        } else {
            io.show("Oh no! I'm sorry, but you don't have a friend to play with. Let's play anyway!");
            EndGame();
        }

    }

    public void PlayGame(Player Executioner, Player Guesser) {
        io.show("The Executioner is " + Executioner.getName());
        io.show("The Guesser is " + Guesser.getName());
        io.show("Executioner please choose a secret word consisting of the 26 letters of the alphabet.");

        SecretWord secretWord = new SecretWord(io.promptForText("What is the secret word?"));

        io.show("The Executioner has chosen the secret word " + secretWord.dashed());

        for (int i = 6; i > 0; i--) {
            io.show("Guesser please guess a letter.");
            String guess = io.promptForText("What is your guess?");

            io.show(secretWord.correct().toString());
        }

    };

    private void EndGame() {
        io.show("Thanks for playing!");
    };

    // private void ShowScore();

    // private void ShowWinner();

}