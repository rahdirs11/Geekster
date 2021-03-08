import java.util.Scanner;

class Stack {
    static int top = -1;
    static final int maxSize = 5;
    static int[] stack = new int[maxSize];
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String options = "1 ----- Push\n2 ----- Pop\n3 ----- Display\n4 ----- Exit\n";
        System.out.print(options + "Choice:\t");
        int choice = scan.nextInt(), value;
        while (choice != 4) {
            switch (choice) {
                case 1:
                    if (top == maxSize - 1) {
                        System.out.println("Stack is full!!");
                    } else {
                        push(value);
                    }
                    break;
                case 2:
                    value = pop();
                    if (value != -1) {
                        System.out.println("Popped element:\t" + value);
                    }
                    break;
                case 3:
                    display();
                    break;
                default:
                    System.out.println("INVALID OPTION!!");
            }
            System.out.print(options + "Choice:\t");
            choice = scan.nextInt();
        }
        System.out.println("You chose to exit!");
    }

    public static void push(int value) {
        stack[++top] = value;
        System.out.println("Top = " + top);
    }

    public static int pop() {
        if (top == -1) {
            System.out.println("STACK IS EMPTY!!");
            return -1;
        } else {
            return stack[--top];
        }
    }

    public static void display() {
        if (top == -1) {
            System.out.println("STACK IS EMPTY!!\nNOTHING TO DISPLAY!!");
        } else {
            System.out.println("Values of stack =>");
            for (int i = 0; i <= top; ++i) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }
    }
}