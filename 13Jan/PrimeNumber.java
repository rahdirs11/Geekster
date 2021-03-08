import java.util.Scanner;
public class PrimeNumber {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter a number:\t");
		int number = scan.nextInt();
		boolean isPrime = true;
		for (int i = 2; i <= Math.sqrt(number); ++i) {
			if (number % i == 0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime) {
			System.out.println("NOT A PRIME NUMBER!!");
		} else {
			System.out.println("PRIME NUMBER!!")
		}
	}
}
