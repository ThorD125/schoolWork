package classes;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CarFactoryTest {

    @Test
    void buildCar() {

        CarFactory autoFabriek = new CarFactory("Volvo", "Gent");
        assertEquals("Volvo-Gent(0)", autoFabriek.toString());
        Cars car1 = autoFabriek.BuildCar();
        assertEquals("Volvo-Gent(1)", autoFabriek.toString());
    }
}