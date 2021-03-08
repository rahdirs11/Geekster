import java.util.Scanner;
public class LargestOfThree {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter three integers =>");
		int a = scan.nextInt(), b = scan.nextInt(), c = scan.nextInt();
		System.out.println("Largest of three:\t" + largestOfThree(a, b, c));
	}
	
	public static int largestOfThree(int a, int b, int c) {
		return a > b? (a > c? a: c): (b > c? b: c);
	}

}
