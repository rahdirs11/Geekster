import java.util.Scanner;
public class DigitCount {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int number = scan.nextInt();
		int temp = number, digits = 0;
		while (temp != 0) {
			++digits;
			temp /= 10;
		}
	}

}
