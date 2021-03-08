import java.util.Scanner;

class SumFirst10 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		// using formula method
		System.out.println("Sum of first 10 natural numbers using formula method:\t" + (10 * 11 / 2));
		// using for-loop
		int sum = 0;
		for (int i = 1; i <= 10; ++i)	sum += i;
		System.out.println("Sum of first 10 natural numbers using for-loops:\t" + sum);
	}
}
