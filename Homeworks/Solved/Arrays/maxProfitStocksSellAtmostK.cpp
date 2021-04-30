#include <iostream>
using namespace std;


int valleyApproach(int arr[], int n) {
	int profit{};
	for (int i = 1; i < n; ++i) {
		int diff = arr[i] - arr[i - 1];
		if (diff > 0) {
			profit += diff;
		}
	}
	return profit;
}



int main() {
	int n{};
	cin >> n;

	int* stocks = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> stocks[i];
	}

	int* profits = new int[n];
	for (int i = 0; i < n; ++i) {
		profits[i] = 0;
	}

	int maxVal{stocks[n - 1]};
	for (int i = n - 2; i >= 0; --i) {
		maxVal = max(maxVal, stocks[i]);
		profits[i] = max(profits[i + 1], maxVal - stocks[i]);
	}

	int minVal{stocks[0]};
	for (int i = 1; i < n; ++i) {
		minVal = min(minVal, stocks[i]);
		profits[i] = max(profits[i - 1], profits[i] + stocks[i] - minVal);
	}

	// cout << profits[n - 1] << endl;
	cout << valleyApproach(stocks, n);

	delete [] stocks;
	delete [] profits;
	return 0;
}

/*
10 22 5 75 65 80

75 75 75 15 15 0

75 87 87 87 87 87 
*/
