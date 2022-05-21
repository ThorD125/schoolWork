package classes;

import java.util.Scanner;

public class IO {

    private final Scanner in = new Scanner(System.in);

    public void show(String txt) {
        System.out.println(txt);
    }

    public String promptForText(String prompt) {
        System.out.print(prompt);
        return in.nextLine();
    }

    public boolean promptForBoolean(String prompt) {
        System.out.print(prompt + " (y/n)");
        String res = in.nextLine();
        while (!(res.equalsIgnoreCase("y") || res.equalsIgnoreCase("n"))) {
            System.out.print("(again)" + prompt + " (y/n)");
            res = in.nextLine();
        }

        return res.equalsIgnoreCase("y");
    }

}
