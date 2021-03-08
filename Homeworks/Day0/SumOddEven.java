import java.util.Scanner;

class SumOddEven {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter 'n' (total number of integers):\t");
    int total = scan.nextInt();
    int sumOdd = 0, sumEven = 0;
    for (int i = 1; i <= total; ++i) {
      System.out.print("\fEnter number " + (i) + ":\t");
      int number = scan.nextInt();
      if (number % 2 == 0) {
        sumEven += number;
      } else {
        sumOdd += number;
      }
    }
    System.out.println("\fSum of odd numbers:\t" + sumOdd + "\nSum of even numbers:\t" + sumEven);
  }
}
