class HI {
    public static void main(String[] args) {
        System.out.println("DONE");
        printHi(5);
    }

    static void printHi(int n) {
        if (n == 0) return;
        if (n % 2 != 0) {
            System.out.println("hi " + n);
            printHi(--n);
        } else {
            printHi(n - 1);
            System.out.println("bye " + n);
        }
    }
}   
