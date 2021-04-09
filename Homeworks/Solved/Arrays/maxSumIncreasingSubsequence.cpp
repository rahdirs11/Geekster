#include <algorithm>
#include <iostream>
using namespace std;


int main() {
	int n{};
	cin >> n;
	int* arr = new int[n], dp = new int[n];
	for (int i = 0; i < n; ++i)  {
		cin >> arr[i];
		dp[i] = arr[i];
	}

	for (int i = 1; i < n; ++i) {
		for (int j = 0; j < i; ++j) {
			if (arr[i] > arr[j] && dp[i] < dp[j] + arr[j]) {
				dp[i] = dp[j] + arr[i];
			}
		}
	}

	cout << *max_element(arr, arr + n) << endl;
	delete [] arr;
	delete [] dp;
	return 0;
}