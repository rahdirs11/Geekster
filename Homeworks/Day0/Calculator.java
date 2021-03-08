import java.util.Scanner;

class Calculator {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter the value of 'a':\t");
    int a = scan.nextInt();
    System.out.print("Enter the value of 'b':\t");
    int b = scan.nextInt();
    System.out.print("\f1 ----- Addition\n2 ----- Subtraction\n3 ----- Multiplication\n4 ----- Division\nChoice:\t");
    int choice = scan.nextInt();
    switch(choice) {
      case 1:
      System.out.println("a + b = " + (a + b));
      break;
      case 2:
      System.out.println("a - b = " + (a - b));
      break;
      case 3:
      System.out.println("a * b = " + (a * b));
      break;
      case 4:
      try {
        System.out.println("a / b = " + (double)(a * 1.0 / b));
      } catch (ArithmeticException e) {
        System.out.println("'b' CANNOT BE 0:\t" + e);
      }
      break;
      default:
        System.out.println("INVALID INPUT!!");
    }
  }
}
