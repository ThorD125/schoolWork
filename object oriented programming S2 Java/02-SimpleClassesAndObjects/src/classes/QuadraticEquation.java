package classes;

public class QuadraticEquation {
    int a;
    int b;
    int c;
    int x;
    int discriminant;

    public QuadraticEquation(int a, int b, int c, int x) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.x = x;
        computeDiscriminant();
    }

    public void computeDiscriminant() {
        this.discriminant = (b * b) - (4 * a * c);
    }

    public String standardform() {
        return a + "*x*x + " + b + "*x + " + c + " = 0";
    }

    public int zeroPointOne() {
        return (int) ((-b - Math.sqrt(discriminant)) / (2 * a));
    }

    public int zeroPointTwo() {
        return (int) ((-b + Math.sqrt(discriminant)) / (2 * a));
    }
}
