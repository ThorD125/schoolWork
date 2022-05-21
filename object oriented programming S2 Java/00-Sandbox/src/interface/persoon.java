package test;

public class persoon /* implements canholditem */ {
    private persoon ourpersoon;
    private item ourItem;

    public persoon getpersoon() {
        return ourpersoon;
    }

    public void addpersoon(persoon mypersoon) {
        this.ourpersoon = mypersoon;
    }

    public item getItem() {
        return ourItem;
    }

    public void addItem(item myItem) {
        this.ourItem = myItem;
    }

}
