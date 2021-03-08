import java.util.Scanner;

class GreatestOfTwo {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter two numbers =>");
    int a = scan.nextInt(), b = scan.nextInt();
    if (a == b) {
      System.out.println("Both are equal");
    } else {
      System.out.println("Greatest between " + a + " and " + b + " is " + (a > b? a: b)));
    }
  }
}
