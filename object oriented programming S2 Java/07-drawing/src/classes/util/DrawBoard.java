package classes.util;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class DrawBoard {

    private static final Color DEFAULT_COLOR = Color.RED;

    private final int width;
    private final int height;
    private final int refreshRate;
    private final int scale;

    private Image img;

    public void draw(int x, int y) {
        this.draw(x, y, DEFAULT_COLOR);
    }

    public DrawBoard(int width, int height, int scale, int refreshRate) {
        this.width = width;
        this.height = height;
        this.refreshRate = refreshRate;
        this.scale = scale;
        initFrame();
    }

    public DrawBoard() {
        this(600, 600, 5, 500);
    }

    private void initFrame() {
        JFrame f = new JFrame("DrawBoard");
        img = new BufferedImage(width, height,BufferedImage.TYPE_INT_ARGB);
        f.add(new JLabel(new ImageIcon(img)));
        f.pack();
        f.setVisible(true);
        f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        new Timer(refreshRate, e -> SwingUtilities.invokeLater(f::repaint)).start();
    }

    private int ox;
    private int oy;

    public void setOrigin(int x, int y) {
        this.ox = scale *x;
        this.oy = scale *y;
    }



    public void draw(int x, int y, Color c) {
        Graphics g =  img.getGraphics();
        g.setColor(c);
        g.fillRect(ox+ scale + scale *x,oy+ scale + scale *y, scale, scale);
        g.dispose();
    }

}
