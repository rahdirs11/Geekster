public class ArrayPrintR {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 10, 20, 60};
        printArray(array, array.length - 1);
    }

    static void printArray(int[] a, int length) {
        if (length == -1) {
            return;
        }
        System.out.println(a[length]);
        printArray(a, length - 1);
    }
    
}
