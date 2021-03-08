import java.util.Scanner;

class LargestOfN {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String continueOption = "Y ----- Continue\nN ----- Exit";
    int max = Integer.MIN_VALUE, total = 0;
    while (true) {
      System.out.print("\fEnter a number:\t");
      int number = scan.nextInt();
      scan.nextLine();
      ++total;
      max = number > max? number: max;
      System.out.println("\f" + continueOption + "\nChoice:\t");
      String choice = scan.nextLine();
      if (Character.toLowerCase(choice.charAt(0)) == 'n') {
        System.out.println("You chose to exit!\nBYE!!");
        break;
      }
    }
    System.out.println("Largest of " + total + " entered numbers is " + max);
  }
}
