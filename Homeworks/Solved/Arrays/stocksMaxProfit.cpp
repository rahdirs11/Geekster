#include <iostream>
#include <limits>
using namespace std;

int main() {
	int n{};
	cin >> n;
	int* stocks = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> stocks[i];
	}

	int currMin = stocks[0], maxProfit{INT_MIN};
	for (int i = 0; i < n; ++i) {
		currMin = min(currMin, stocks[i]);

		int diff = stocks[i] - currMin;
		maxProfit = max(diff, maxProfit);
	}
	cout << maxProfit << endl;
	return 0;
}