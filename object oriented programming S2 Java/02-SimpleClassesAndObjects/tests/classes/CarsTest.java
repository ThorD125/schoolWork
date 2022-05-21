package classes;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CarsTest {
    private Cars auto() {
        Cars auto = new Cars("Volvo", "red", 500);

        return  auto;
    }

    @Test
    void repaint() {
        Cars car = auto();
        car.repaint("purple");
        assertEquals("purple", car.getColor());
    }
}

