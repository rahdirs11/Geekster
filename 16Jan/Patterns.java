import java.util.Scanner;

class Patterns {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    // printPatternOne(4);
    // printPatternTwo(4);
    // printPatternThree(4);
    // printPatternFour(10);
    // printPatternFive(4);
    printPatternSix(4);
  }

  public static void printPatternOne(int lines) {
    System.out.println("Pattern 1 =>");
    for (int i = 1; i <= lines; ++i) {
      for (int j = 1; j <= i; ++j)
        System.out.print('*');
      System.out.println();
    }
  }

  public static void printPatternTwo(int rows) {
    System.out.println("Pattern 2 =>");
    int row = 1;
    while (row <= rows) {
      int num = 1;
      while (num <= row) {
        System.out.print(num + " ");
        ++num;
      }
      System.out.println();
      ++row;
    }
  }

  public static void printPatternThree(int lines) {
    int item = 1;
    int row = 1;
    while (row <= lines) {
      int line = 1;
      while (line <= row) {
        System.out.print(item + " ");
        ++item;
        ++line;
      }
      System.out.println();
      ++row;
    }
  }

  public static void printPatternFour(int line) {
    int row = line, nst = 1;
    while (row >= 1) {
      int spaces = row - 1;
      while (spaces >= 1) {
        System.out.print(" ");
        --spaces;
      }
      int cst = 1;
      while (cst <= nst) {
        System.out.print("*");
        ++cst;
      }
      System.out.println();
      --row;
      ++nst;
    }
  }

  public static void printPatternFive(int line) {
    int nst = 1, row = 1, cst = 1;
    while (row <= line) {
      cst = 1;
      int spaces = line - row;
      while (spaces >= 1) {
        System.out.print(' ');
        --spaces;
      }
      while (cst <= nst) {
        System.out.print("*");
        ++cst;
      }
      nst = row - 1;
      cst = 1;
      while (cst <= nst) {
        System.out.print("*");
        ++cst;
      }
      ++row;
      nst = row;
      System.out.println();
    }
  }

  public static void printPatternSix(int line) {
    int row = 1, nst = 1, cst = 1;
    while (row <= 2 * line - 1) {
      int spaces = row <= line? line - row: row - line;
      while (spaces >= 1) {
        System.out.print(" ");
        --spaces;
      }
      cst = 1;
      while (cst <= (int)(nst / 2) + 1) {
        System.out.print("*");
        ++cst;
      }
      cst = 1;
      while (cst <= (int)(nst / 2)) {
        System.out.print('*');
        ++cst;
      }
      nst = row < line? nst + 2: nst - 2;
      ++row;
      System.out.println();
    }
  }
}
