import java.util.Scanner;

class Stocks {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Enter total number of days:\t");
    int days = scan.nextInt(), stocks[] = new int[days];
    System.out.println("Enter the stock values on all of the " + days + " days");
    for (int i = 0; i < days; ++i) {
      stocks[i] = scan.nextInt();
    }
    calculateMaxProfit(stocks);
  }

  public static void calculateMaxProfit(int[] stocks) {
    int buyDay = 0, sellDay = 0;
    int currentMin = stocks[0], profit = 0;
    int maxProfit = 0;
    for (int i = 1; i < stocks.length; ++i) {
      if (stocks[i] >= currentMin) {
        profit = stocks[i] - currentMin;
        if (maxProfit <= profit) {
          maxProfit = profit;
          sellDay = i;
        }
      }
      if (stocks[i] < currentMin) {
          currentMin = stocks[i];
          buyDay = i;
      }
    }
    System.out.println("Max profit (possible):\t" + (maxProfit));
    System.out.println("Buy on day " + (1 + buyDay) + "\nSell on day " + (maxProfit == 0? buyDay + 1: 1 + sellDay));
``  }
}
