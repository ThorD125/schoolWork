package s8;

import java.util.Objects;

public class Address implements Comparable<Address>{

    private String address;

    public Address(String GivenAddress){
        this.address = GivenAddress;
    }

    @Override
    public String toString(){
        return address;
    }

    @Override
    public int hashCode() {
        return address != null ? address.hashCode() : 0;
    }

//    @Override
    public boolean equals(Address obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Address person = (Address) obj;

        return Objects.equals(address, obj.address);
    }

    @Override
    public int compareTo(Address other) {
        return address.compareTo(other.address);
    }
}
