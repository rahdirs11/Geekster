import java.util.Scanner;

class Grades {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter your score:\t");
    int marks = scan.nextInt();
    char grade = '\u0000';
    if (marks <= 25) {
      grade = 'F';
    } else if (marks > 25 && marks <= 45) {
      grade = 'E';
    } else if (marks > 45 && marks <= 50) {
      grade = 'D';
    } else if (marks > 50 && marks <= 60) {
      grade = 'C';
    } else if (marks > 60 && marks <= 80) {
      grade = 'B';
    } else if (marks > 80 && marks <= 100) {
      grade = 'A';
    } else {
      System.out.println("INVALID MARKS!!\nMarks should be [0, 100]");
      System.exit(1);
    }
    System.out.println("Grades:\t" + grade);
  }
}
