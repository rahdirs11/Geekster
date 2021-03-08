import java.util.Scanner;

class PDFViewer {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int[] h = new int[26];
    String word;
    for (int i = 0; i < 26; ++i)
      h[i] = scan.nextInt();
    scan.nextLine();
    word = scan.nextLine();
    System.out.println(designerPdfViewer(h, word));
  }

  static int designerPdfViewer(int[] h, String word) {
    int maxHeight = 0;
    for (int i = 0; i < word.length(); ++i) {
      char ch = word.charAt(i);
      maxHeight = h[ch - 97] >= maxHeight? h[ch - 97]: maxHeight;
    }
    return word.length() * maxHeight;
  }
}
