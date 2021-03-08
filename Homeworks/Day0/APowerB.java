import java.util.Scanner;

class APowerB {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter two numbers:\t");
		int a = scan.nextInt(), b = scan.nextInt();
		System.out.println("First number raised to second number:\t" + power(a, b));
	}

	public static int power(int a, int b) {
		if (b == 0) {
			return 1;
		}
		if (b % 2 == 0) {
			return power(a * a, b / 2);
		} else {
			return a * power(a, b - 1);
		}
	}
}
