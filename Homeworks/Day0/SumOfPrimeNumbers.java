import java.util.Scanner;

class SumOfPrimeNumbers {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter the limit:\t");
    int n = scan.nextInt();
    boolean[] numbers = new boolean[n + 1];
    for (int i = 2; i <= n; ++i) {
      numbers[i] = true;
    }
    int v = 2;
    while (v * v <= n) {
      if (numbers[v]) {
        for (int j = v * v; j <= n; j += v) {
          numbers[j] = false;
        }
      }
      ++v;
    }
    int sum = 0;
    for (int i = 2; i <= n; ++i) {
      if (numbers[i]) {
        // System.out.print(i + " ");
        sum += i;
      }
    }
    System.out.println("\fSum of all prime numbers upto " + n + " is " + sum);
  }
}
