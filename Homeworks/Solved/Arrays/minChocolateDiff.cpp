/*
Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int minChocolates(vector<int>, int);

int main() {
	int n{}, m{};
	cin >> n;
	vector<int> chocolates(n);
	for (int i = 0; i < n; ++i) {
		cin >> chocolates[i];
	}	// chocolate packets

	cin >> m;	// number of students

	cout << minChocolates(chocolates, m) << endl;
	return 0;
}

int minChocolates(vector<int> chocolates, int m) {
	sort(chocolates.begin(), chocolates.end());
	int minDiff{INT_MAX};
	for (int i = 0; i + m - 1 < chocolates.size(); ++i) {
		int diff = chocolates[i + m - 1] - chocolates[i];
		minDiff = min(minDiff, diff);
	}
	return minDiff;
}