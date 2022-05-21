package s8;

import java.util.Objects;

public class Contact implements Comparable<Contact>{

    private String name;

    public Contact(String givenName){
        this.name = givenName;
    }

    @Override
    public String toString(){
        return name;
    }

    @Override
    public int hashCode() {
        return name != null ? name.hashCode() : 0;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Contact person = (Contact) obj;

        return Objects.equals(name, person.name);
    }

    @Override
    public int compareTo(Contact other) {
        return name.compareTo(other.name);
    }
}
