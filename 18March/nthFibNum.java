import java.util.*;

public class DP {
  public static void main(String[] args) {
    Scanner obj = new Scanner(System.in);
    int n = obj.nextInt();
    long [] dp = new long[n + 2];
    for (int i = 1; i <= n; ++i) {
      dp[i] = -1;
    }
    // System.out.println(fib(n));
    System.out.println(fibImproved(n, dp));
  }

  public static int fib(int n) {
    if (n == 1 || n == 2) {
      return n - 1;
    }
    return fib(n - 1) + fib(n - 2);
  } // recursive solution

  public static long fibImproved(int n, long[] dp) {
    if (dp[n] != -1) {
      return dp[n];
    }
    if (n == 1 || n == 2) {
      return n - 1;
    }
    long f1 = fibImproved(n - 1, dp), f2 = fibImproved(n - 2, dp);
    dp[n] = f1 + f2;
    return dp[n];
  }
}
