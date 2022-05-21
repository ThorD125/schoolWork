package s00;

public class HelloWorld {
    public static void main(String[] args) {
        new HelloWorld().run();
    }

    void run() {
        System.out.println("Hello World");

        String text = "text";
        int number = 1;
        System.out.println(text);
        System.out.println(number);

        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }

        int j = 0;
        while (j < 10) {
            System.out.println(j);
            j++;
        }

        if (10 == j) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

    }
}
