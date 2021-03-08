public class Fibonacci {
    public static void main(String[] args) {
        System.out.println(fibonacci(10));
    }

    static int fibonacci(int n) {
        if (n == 1 || n == 0) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    
}
