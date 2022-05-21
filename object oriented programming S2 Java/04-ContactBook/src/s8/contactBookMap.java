package s8;

import java.util.HashMap;
import java.util.Map;

public class contactBookMap implements ContactBook {

    private Map<Contact, Address> phonebook = new HashMap<>();


    @Override
    public void add(Contact newContact, Address newAddress) {
        phonebook.put(newContact, newAddress);
    }

    @Override
    public void remove(Contact name) {
        phonebook.remove(name);
    }

}
