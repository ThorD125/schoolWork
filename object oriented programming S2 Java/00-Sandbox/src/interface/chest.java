package test;

public class chest /* implements canholditem */ {
    private item ourItem;

    public item getItem() {
        return ourItem;
    }

    public void addItem(item myItem) {
        this.ourItem = myItem;
    }

}
