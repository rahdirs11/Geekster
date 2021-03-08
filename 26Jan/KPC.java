import java.util.ArrayList;

public class KPC {
    public static void main(String[] args) {
        for (String r: getKPC("23")) {
            System.out.println(r);
        }
        System.out.println(getKPC("456").toString());
    }

    static ArrayList<String> getKPC(String str) {
        if (str.length() == 0) {
            ArrayList<String> r = new ArrayList<String>();
            r.add("");
            return r;
        }

        char ch = str.charAt(0);
        String rest = str.substring(1);
        ArrayList<String> recursive = getKPC(rest);
        ArrayList<String> result = new ArrayList<String>();
        String choice = choice(ch);
        for (String r: recursive) {
            for (int i = 0; i < choice.length(); ++i) {
                String string = choice.charAt(i) + r;
                result.add(string);
            }
        }
        return result;
    }

    static String choice(char ch) {
        switch(ch) {
            case '2':
                return "abc";
            case '3':
                return "def";
            case '4':
                return "ghi";
            case '5':
                return "jkl";
            case '6':
                return "mno";
            case '7':
                return "pqrs";
            case '8':
                return "tuv";
            case '9':
                return "wxyz";
        }
        return "";
    }
}
