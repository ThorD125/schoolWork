package classes;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TallyTest {

    @Test
    void testEquals() {
        Tally tally1 = new Tally();
        Tally tally2 = new Tally();
        Tally tally3 = new Tally();
        Tally tally4 = new Tally(500);
        tally3.incr();
        assertEquals(tally1, tally2);
        assertNotEquals(tally1, tally3);
        assertNotEquals(tally3, tally4);
    }

}