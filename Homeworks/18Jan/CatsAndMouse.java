import java.util.Scanner;

class CatsAndMouse {
  public static void main(String[] args) {
    Scanner = new Scanner(System.in);
    int t = scan.nextInt();
    while (t > 0) {
      int x = scan.nextInt(), y = scan.nextInt(), z = scan.nextInt();
      System.out.println(catAndMouse(x, y, z));
      --t;
    }
  }

  static String catAndMouse(int x, int y, int z) {
    int catA = Math.abs(z - x), catB = Math.abs(y - z);
    if (catA == catB) {
      return "Mouse C";
    } else if (catA > catB) {
      return "Cat B";
    } else {
      return "Cat A";
    }
  }
}
