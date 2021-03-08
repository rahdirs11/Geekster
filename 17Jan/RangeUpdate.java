import java.util.Scanner;

class RangeUpdate {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter number of queries:\t");
    int q = scan.nextInt();
    System.out.print("Enter size of array:\t");
    int size = scan.nextInt();
    // int[] array = new int[size];
    int[] prefixSum = new int[size];
    while (q >= 1) {
      System.out.println("Enter l and r (0-based index)=>");
      int l = scan.nextInt(), r = scan.nextInt();
      System.out.print("Enter the update value:\t");
      int value = scan.nextInt();
      prefixSum[l] += value;
      prefixSum[r + 1] -= value;
      --q;
    }
    calculatePrefixSum(prefixSum);
  }

  public static void calculatePrefixSum(int[] prefixSum) {
    for (int i = 1; i < prefixSum.length; ++i) {
      prefixSum[i] += prefixSum[i - 1];
    }
    printArray(prefixSum);
  }

  public static void printArray(int[] prefixSum) {
    for (int value: prefixSum) {
      System.out.println(value + " ");
    }
  }
}
