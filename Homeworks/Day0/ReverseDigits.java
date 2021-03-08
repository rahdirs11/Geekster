import java.util.Scanner;

class ReverseDigits {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter the number to be reversed:\t");
    int number = scan.nextInt();
    int temp = number, reverse = 0;
    while (temp != 0) {
      reverse = (reverse * 10) +  (temp % 10);
      temp /= 10;
    }
    System.out.println("Reverse of " + number + " is " + reverse);
  }
}
