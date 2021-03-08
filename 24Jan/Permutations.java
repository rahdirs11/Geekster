import java.util.ArrayList;

public class Permutations {
    public static void main(String[] args) {
        for (String perm: getPermutation("abc")) {
            System.out.print(perm + " ");
        }
    }

    static ArrayList<String> getPermutation(String str) {
        if (str.length() == 0) {
            ArrayList<String> list = new ArrayList<String>();
            list.add("");
            return list;
        }

        char ch = str.charAt(0);
        String rest = str.substring(1);
        ArrayList<String> remaining = getPermutation(rest);
        ArrayList<String> current = new ArrayList<String>();
        for (String s: remaining) {
            for (int i = 0; i < s.length() + 1; ++i) {
                String c = s.substring(0, i) + ch + s.substring(i);
                current.add(c);
            }
        }
        return current;
    }
}
