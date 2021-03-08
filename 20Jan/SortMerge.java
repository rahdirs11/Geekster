import java.util.*;

class SortMerge {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Integer> arr1 = new ArrayList<Integer>(Arrays.asList(1, 3, 5, 6)), arr2 = new ArrayList<Integer>(Arrays.asList(5, 6, 7, 12, 20));
        ArrayList<Integer> merged = new ArrayList<Integer>();
        merged = mergeTwoSorted(arr1, arr2);
        for (int i: merged) {
            System.out.print(i + " ");
        }
        System.out.println();
        scan.close();
    }

    static ArrayList<Integer> mergeTwoSorted(ArrayList<Integer> arr1, ArrayList<Integer> arr2) {
        int i = 0, j = 0;
        ArrayList<Integer> merged = new ArrayList<Integer>();
        while (i < arr1.size() && j < arr2.size()) {
            if (arr1.get(i) <= arr2.get(j)) {
                merged.add(arr1.get(i++));
            } else {
                merged.add(arr2.get(j++));
            }
        }
        if (i < arr1.size()) {
            while (i < arr1.size()) {
                merged.add(arr1.get(i++));
            }
        } else if (j < arr2.size()) {
            while (j < arr2.size()) {
                merged.add(arr2.get(j++));
            }
        }
        return merged;
    }
}