package classes;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
class PersonTest {


    @Test
    void testEquals() {
        Person me = new Person("Mattias");
        Person me2 = new Person("Mattias", 25);
        Person me3 = new Person("Mattias");
        assertFalse(me.equals(me2));
        assertTrue(me.equals(me3));
    }

    @Test
    void getName() {
        Person me = new Person("Mattias");
        assertEquals("Mattias", me.getName());
    }

    @Test
    void celebrateBirthday() {
        Person me = new Person("Mattias");
        assertEquals(0, me.getAge());;
        me.celebrateBirthday();
        assertEquals(1, me.getAge());
    }

}