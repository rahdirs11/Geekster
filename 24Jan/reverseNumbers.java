import java.util.Scanner;

class ReverseNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        printNumbers(n);
        scan.close();
    }

    static void printNumbers(int n) {
        if (n == 1) {
            System.out.println(n);
            return;
        }
        System.out.print(n + ", ");
        printNumbers(--n);
    }
}