import java.util.Scanner;

class CutSticks {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int[] sticks = new int[n];
    for (int i = 0; i < n; ++i) {
      sticks[i] = scanner.nextInt();
    }
    int[] sticksCount = cutTheSticks(sticks);
    for (int stick: sticksCount) {
      if (stick != 0)
        System.out.println(stick);
    }
    scanner.close();
  }

  static int findMin(int[] arr) {
    int min = Integer.MAX_VALUE;
    for (int i: arr) {
      if (i != 0 && i < min) {
        min = i;
      }
    }
    return min;
  }

  static int[] cutTheSticks(int[] sticks) {
    int[] sticksCount = new int[sticks.length];
    int index = -1, shortestStick = 0;
    int length = sticks.length, newLength = 0;
    sticksCount[++index] = length;
    while (length != 0) {
      newLength = 0;
      shortestStick = findMin(sticks);
      for (int i = 0; i < sticks.length; ++i) {
        if (sticks[i] != 0) {
          sticks[i] -= shortestStick;
          if (sticks[i] != 0) {
            ++newLength;
          }
        }
      }
      if (newLength != 0) {
        sticksCount[++index] = newLength;
      }
      length = newLength;
    }
    return sticksCount;
  }
}
