import java.util.Scanner;

class DivisorCount {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println(findDigits(scan.nextInt()));
  }

  static int findDigits(int n) {
    int divisorCount = 0, d, temp = n;
    while (temp > 0) {
      d = temp % 10;
      if (d != 0 && n % d == 0) {
        ++divisorCount;
      }
      temp /= 10;
    }
    return divisorCount;
  }
}
