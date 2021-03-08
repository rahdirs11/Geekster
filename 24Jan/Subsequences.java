import java.util.ArrayList;
public class Subsequences {
    public static void main(String[] args) {
        for (String s: subsequences("abcd")) {
            System.out.println(s);
        }
    }

    static ArrayList<String> subsequences(String s) {
        if (s.length() == 0) {
            ArrayList<String> result = new ArrayList<String>();
            result.add("");
            return result;
        }
        char ch = s.charAt(0);
        ArrayList<String> rest = subsequences(s.substring(1));
        ArrayList<String> preset = new ArrayList<String>();
        for (String x: rest) {
            preset.add(x);
            preset.add(ch + x);
        }
        return preset;
    }
}
