package classes;

import java.awt.*;

public class Rectangle extends Shape {
    private int width;
    private int height;

    public Rectangle(int x0, int y0, Color fillColor, Color borderColor, int width, int height) {
        super(x0, y0, fillColor, borderColor);
        this.width = width;
        this.height = height;
    }


    public boolean isPartOfShape(int i, int j) {
        return i>=0 && j >= 0 && i < width && j < height;
    }

    public int getMaxHeight() {
        return height;
    }

    public int getMaxWidth() {
        return width;
    }

}
