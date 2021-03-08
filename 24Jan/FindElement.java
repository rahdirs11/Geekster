public class FindElement {
    public static void main(String[] args) {
        int[] arr = {5, 10, 20, 30, 40, 10};
        System.out.println("First index:\t" + (findFirstIndex(arr, 10, 0) + 1) + "\nLast index:\t" + (findLastIndex(arr, 10, arr.length - 1) + 1));
        int[] positions = findIndices(arr, 10, 0, 0);
        for (int a: positions) {
            if (a != 0) {
                System.out.print(a + " ");
            }
        }
    }

    static int findFirstIndex(int[] arr, int key, int index) {
        if (index == arr.length) {
            return -1;
        }
        if (arr[index] == key) {
            return index;
        }
        return findFirstIndex(arr, key, index + 1);
    }

    static int findLastIndex(int[] arr, int key, int index) {
        return index == -1? -1: (arr[index] == key? index: findLastIndex(arr, key, index - 1));
    }

    static int[] findIndices(int[] arr, int key, int index, int found) {
        if (index == arr.length)
            return new int[found];
        if (arr[index] == key) {
            int[] a = findIndices(arr, key, index + 1, found + 1);
            a[found] = index;
            return a;
        } else {
            return findIndices(arr, key, index + 1, found);
        }
    }
}
