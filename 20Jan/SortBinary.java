import java.util.*;

public class SortBinary {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> binary = new ArrayList<Integer>(Arrays.asList(1, 1, 1, 0, 1, 1, 1, 1, 1, 0));
        int left = binary.indexOf(1), right = binary.lastIndexOf(0);
        while (left < right) {
            int temp = binary.get(left);
            binary.set(left, binary.get(right));
            binary.set(right, temp);
            left = binary.indexOf(1);
            right = binary.lastIndexOf(0);
        }
        for (int bit: binary) {
            System.out.print(bit + " ");
        }
        System.out.println();
        scanner.close();
    }
    
}
