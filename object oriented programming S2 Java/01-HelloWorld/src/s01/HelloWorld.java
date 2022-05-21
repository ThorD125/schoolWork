package s01;

import java.util.Arrays;
import java.util.List;

public class HelloWorld {
    public static void main(String[] args) {
        new HelloWorld().run();
    }

    void run() {
        System.out.println("Hello World");
        System.out.println(sum(1, 2));
        // System.out.println(reverse("teskjfkme"));
        System.out.println(Arrays.toString(decompose(12346)));
    }

    int sum(int a, int b) {
        return a + b;
    }

    String reverse(String txt) {
        String res = "";
        for (int i = 0; i < txt.length(); i++) {
            res = txt.charAt(i) + res;
        }
        return res;
    }

    boolean is_palindrome(String txt) {
        return txt == reverse(txt);
    }

    String sub_str(String txt, int lo, int high) {
        String res = "";
        for (int i = lo; i < txt.length(); i++) {
            res += txt.charAt(i);
        }
        return res;
    }

    int find(String haystack, String needle) {
        for (int i = 0; i < haystack.length() - needle.length(); i++) {
            if (sub_str(haystack, i, i + needle.length()).equals(needle)) {
                return i;
            }
        }
        return -1;
    }

    String[] decompose(int n) {
        String str = Integer.toString(n);

        String res[] = new String[str.length()];

        for (int i = 0; i < str.length(); i++) {
            res[i] = Character.toString(str.charAt(i));
        }
        return res;
    }
}