public class Power {
    public static void main(String[] args) {
        System.out.println(apowerb(2, 5));
    }

    static int apowerb(int a, int b) {
        if (b == 0) {
            return 1;
        }
        if (b % 2 == 0) {
            return apowerb(a * a, b / 2);
        } else {
            return a * apowerb(a, b - 1);
        }
    }
}
