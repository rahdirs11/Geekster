import java.util.Scanner;

class NaturalNumbersReverse {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter the value of 'n':\t");
    int n = scan.nextInt();
    int i = n;
    while (i > 0) {
      if (i == 1) {
        System.out.println(i);
      } else {
        System.out.print(i + ", ");
      }
      --i;
    }
  }
}
