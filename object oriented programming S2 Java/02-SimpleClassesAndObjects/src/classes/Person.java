package classes;

public class Person {

    private String name;
    private int age;

    public Person() {
        System.out.println("Please set a name with the setter");
        this.age = 0;
    }

    // default constructor
    // public Person setPerson(String name) {
    // Person me = new Person();
    // me.name = name;
    // me.age = 0;
    // return me;
    // }

    // constructor with parameters
    public /* Person set */ Person(String name) {
        // Person me = new Person();
        /* me. */this.name = name;
        /* me. */this.age = 0;
        // return me;
    }

    public boolean equals(Person other) {
        return this.name == other.name && this.age == other.age;
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public void celebrateBirthday() {
        age++;
        // this.age++;
    }

    public String toString() {
        return name + " (" + age + ")";
    }

}
