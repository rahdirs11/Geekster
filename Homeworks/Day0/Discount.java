import java.util.Scanner;

class Discount {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter the quantity of items :\t");
    int quantity = scan.nextInt();
    double amount = quantity * 100;
    System.out.println("Total Cost:\t" + (quantity <= 10? amount: amount * .9));
  }
}
