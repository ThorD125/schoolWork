package classes;

import classes.util.DrawBoard;

import java.awt.*;

public class Bitmap implements Drawable {

    private static final Color W = Color.WHITE;
    private static final Color B = Color.BLACK;
    private static final Color G = Color.GRAY;
    private static final Color R = Color.RED;

    private final Color[][] pixels = new Color[][]{
            new Color[]{W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
            new Color[]{W, W, W, W, W, W, B, B, B, B, B, B, W, W, W, W, W, W},
            new Color[]{W, W, W, W, B, B, R, R, R, R, W, W, B, B, W, W, W, W},
            new Color[]{W, W, W, B, W, W, R, R, R, R, W, W, W, W, B, W, W, W},
            new Color[]{W, W, B, W, W, R, R, R, R, R, R, W, W, W, W, B, W, W},
            new Color[]{W, W, B, W, R, R, W, W, W, W, R, W, W, W, W, B, W, W},
            new Color[]{W, B, R, R, R, W, W, W, W, W, W, R, R, R, R, R, B, W},
            new Color[]{W, B, R, R, R, W, W, W, W, W, W, R, R, W, W, R, B, W},
            new Color[]{W, B, W, R, R, W, W, W, W, W, W, R, W, W, W, W, B, W},
            new Color[]{W, B, W, W, R, R, W, W, W, W, R, R, W, W, W, W, B, W},
            new Color[]{W, B, W, W, R, R, R, R, R, R, R, R, R, W, W, R, B, W},
            new Color[]{W, B, W, R, R, B, B, B, B, B, B, B, B, R, R, R, B, W},
            new Color[]{W, W, B, B, B, G, G, B, G, G, B, G, G, B, B, B, W, W},
            new Color[]{W, W, W, B, G, W, W, B, W, W, B, W, W, G, B, W, W, W},
            new Color[]{W, W, W, B, W, W, W, W, W, W, W, W, W, W, B, W, W, W},
            new Color[]{W, W, W, W, B, W, W, W, W, W, W, W, W, B, W, W, W, W},
            new Color[]{W, W, W, W, W, B, B, B, B, B, B, B, B, W, W, W, W, W},
            new Color[]{W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
    };


    @Override
    public void drawOnto(DrawBoard db) {
        for (int row = 0; row< pixels.length ; row++) {
            for (int col = 0; col< pixels[row].length ; col++) {
                int x = col;
                int y = row;
                db.draw(x,y, pixels[row][col]);
            }
        }
    }
}

