package classes;

import classes.util.DrawBoard;

import java.awt.*;

public abstract class Shape implements Drawable{
    private final int x0;
    private final int y0;
    private final Color fillColor;
    private final Color borderColor;

    public Shape(int x0, int y0, Color fillColor, Color borderColor) {
        this.x0 = x0;
        this.y0 = y0;
        this.fillColor = fillColor;
        this.borderColor= borderColor;
    }

    public int getX0() {
        return x0;
    }

    public int getY0() {
        return y0;
    }

    public Color getFillColor() {
        return fillColor;
    }

    @Override
    public void drawOnto(DrawBoard db) {
        for (int i = 0; i < getMaxWidth() ; i++) {
            for (int j = 0; j < getMaxHeight() ; j++) {
                if (isPartOfShape(i, j)) {
                    db.draw(i+getX0(), j + getY0(), getFillColor());
                }

                if (isPartOfBorder(i,j)) {
                    db.draw(i+getX0(), j + getY0(), borderColor);
                }
            }
        }
    }

    private boolean isPartOfBorder(int i, int j) {
        return isPartOfShape(i,j) && (!isPartOfShape(i,j+1) || !isPartOfShape(i,j-1) || !isPartOfShape(i+1,j) || !isPartOfShape(i-1,j));
    }

    protected abstract boolean isPartOfShape(int i, int j);

    protected abstract int getMaxHeight();

    protected abstract int getMaxWidth();
}
