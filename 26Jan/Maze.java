import java.util.ArrayList;

public class Maze {
    public static void main(String[] args) {
        for (String r: getMaze(0, 0, 2, 2))
            System.out.println(r + " ");
    }

    static ArrayList<String> getMaze(int cr, int cc, int er, int ec) {
        if (cr == er && cc == ec) {
            ArrayList<String> res = new ArrayList<String>();
            res.add("");
            return res;
        }

        if (cr > er || cc > ec) {
            ArrayList<String> res = new ArrayList<String>();
            return res;
        }

        ArrayList<String> mr = new ArrayList<String>();
        for (int i = 1; i <= ec; ++i) {
            ArrayList<String> rrh = getMaze(cr, cc + i, er, ec);
            for (String r: rrh) {
                mr.add("H" + i + r);
            }
        }

        for (int i = 1; i <= er; ++i) {
            ArrayList<String> rrv = getMaze(cr + i, cc, er, ec);
            for (String r: rrv) {
                mr.add("V" + i + r);
            }
        }

        for (int i = 1; i <= ec && i <= er; ++i) {
            ArrayList<String> rrd = getMaze(cr + i, cc + i, er, ec);
            for (String r: rrd) {
                mr.add("D" + i + r);
            }
        }
        return mr;
    }
}
