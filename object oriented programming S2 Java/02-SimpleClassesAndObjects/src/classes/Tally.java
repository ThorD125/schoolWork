package classes;

import java.util.Objects;

public class Tally implements Comparable<Tally> {

    private int count;
    private int max;

    public Tally() {
        count = 0;
        max = 999;
    }

    public Tally(int maxGiven){
        count = 0;
        max = maxGiven;
    }

    public void incr() {
        count++;
        if (count > 999) {
            count = 0;
        }
    }

    public void decr() {
        count--;
    }

    public void reset() {
        count = 0;
    }

    public int read() {
        return count;
    }

    public String toString() {
        if (count > 1000) {
            return "999";
        } else if (count > 100) {
            return "0" + count;
        } else if (count > 10) {
            return "00" + count;
        } else if (count > 0) {
            return "000" + count;
        } else {
            return "0000";
        }
    }

    @Override
    public int hashCode() {
        return Objects.hash(count, max);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Tally other = (Tally) obj;
        return count == other.count && max == other.max;
    }


    @Override
    public int compareTo(Tally oth) {
        return Integer.compare(count, oth.count);
    }
}
