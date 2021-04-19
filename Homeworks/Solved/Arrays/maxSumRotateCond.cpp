// Given an array arr[] of n integers, find the maximum that maximizes the sum of the value of i*arr[i] where i varies from 0 to n-1.

#include <iostream>
using namespace std;

int main() {
	int n{}, total{};
	cin >> n;
	int* arr = new int[n];
	int currSum{};
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
		total += arr[i];
		currSum += arr[i] * i;
	}

	int output{currSum}, nextSum{};
	for (int i = 1; i < n; ++i) {
		nextSum = currSum - (total - arr[i - 1]) + (arr[i - 1] * (n - 1));
		output = max(output, nextSum);
		currSum = nextSum;
	} 

	cout << output << endl;
	delete [] arr;
	return 0;
}