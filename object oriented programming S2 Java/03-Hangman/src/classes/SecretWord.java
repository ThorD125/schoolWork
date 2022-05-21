package classes;

public class SecretWord {
    private String word;
    private String[] letters;
    private String dashedWord;

    public SecretWord(String wordGiven) {
        this.word = wordGiven;
        this.dashedWord = dashed();
    }

    public Boolean correct() {
        return word.equals(dashedWord);
    }

    public String dashed() {
        return this.dashed(word);
    }

    public String dashed(String word) {
        int wordlength = word.length();
        String lettersdashed = "";

        for (int i = 0; i < wordlength; i++) {
            lettersdashed = lettersdashed + "-";
        }

        return lettersdashed;
    }
}
