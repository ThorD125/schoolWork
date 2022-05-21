package classes;


import classes.util.DrawBoard;

import java.awt.*;
import java.util.List;

public class StartUp {

    public static void main(String[] args) {
        new StartUp().run();
    }

    private void run() {
        DrawBoard db = new DrawBoard();

        List<Drawable> toDraw = List.of(
//                new Bitmap(),
//                new Rectangle(20, 30, Color.ORANGE, Color.BLUE, 100, 45),
//                new Rectangle(30, 0, Color.BLUE, Color.WHITE, 50, 150),
                new Triangle(30, 0, Color.BLUE, Color.WHITE, 50, 150)
        );

        for (Drawable d : toDraw) {
            d.drawOnto(db);
        }




    }

}
