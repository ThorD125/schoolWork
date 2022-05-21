package classes;

public class StartUp {

    public static void main(String[] args) {
        new StartUp().run();
    }

    void run() {
        //autoFabriek();
        // auto();
        // Tallie();
        // persoon();
        // bank();
        // vierkanten();
    }


    private void Tallie() {
        Tally tallie = new Tally();
        System.out.println(tallie);
        System.out.println(tallie.read());
    }

    private void vierkanten() {

        QuadraticEquation qe = new QuadraticEquation(1, 2, 3, 4);
        System.out.println(qe.standardform());
        Person ther = new Person("Ther");
        System.out.println(ther.getName());
        ther.celebrateBirthday();
        System.out.println(ther.toString());

    }

}
