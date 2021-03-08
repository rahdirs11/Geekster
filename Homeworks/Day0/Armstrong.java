import java.util.Scanner;

class Armstrong {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter a number:\t");
    int n = scan.nextInt();
    int temp = n, n2 = 0;
    while (temp != 0) {
      int d = temp % 10;
      n2 += (int)(Math.pow(d, 3));
      temp /= 10;
    }
    System.out.println(n2 == n? "ARMSTRONG NUMBER!!": "NOT ARMSTRONG NUMBER!!");
  }
}
