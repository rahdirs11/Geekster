import java.util.Scanner;

class Bonus {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter current salary:\t");
    double salary = scan.nextDouble();
    System.out.print("Enter total years of service:\t");
    int years = scan.nextInt();
    if (years > 5) {
      System.out.println("You get a bonus of " + (salary * .05));
    } else {
      System.out.println("You don't get a bonus!!");
    }
  }
}
