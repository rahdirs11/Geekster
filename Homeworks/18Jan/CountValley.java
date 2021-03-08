import java.util.Scanner;

class CountValley {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int steps = scan.nextInt();
    scan.nextLine();
    String path = scan.nextLine();
    int valleyCount = countingValleys(steps, path);
    System.out.println(valleyCount);
  }

  public static int countingValleys(int steps, String path) {
    int mountain = 0, valley = 0, countValley = 0;
    int i = 0;
    while (i < path.length()) {
      char p = path.charAt(i);
      if (p == 'U') {
        if (valley == 0) {
          ++mountain;
        } else {
          --valley;
          if (valley == 0) {
            ++countValley;
          }
        }
      } else {
        if (mountain == 0) {
          ++valley;
        } else {
          --mountain;
        }
      }
      ++i;
    }
    return countValley;
  }
}
