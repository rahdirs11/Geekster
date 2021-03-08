import java.util.Scanner;

class RectangleOrSquare {
  public static void main(String[] args) {
    // System.out.println(args);
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter the length and width of the rectangle =>");
    int l = scan.nextInt(), b = scan.nextInt();
    if (l == b) {
      System.out.println("It is a square!!");
    } else {
      System.out.println("It is just a rectangle");
    }
  }
}
