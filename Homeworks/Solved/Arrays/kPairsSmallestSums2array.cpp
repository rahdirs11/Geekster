#include <iostream>
#include <vector>
#include <limits>
#include <string.h>
using namespace std;

vector<vector<int>> pairs(int arr1[], int n1, int arr2[], int n2, int k) {
	int index[n1];
	memset(index, 0, sizeof(index));

	vector<vector<int>> output;
	while (k > 0) {
		int minSum{INT_MAX}, minIdx{0};
		for (int i = 0; i < n1; ++i) {
			if (index[i] < n2 && minSum > arr2[index[i]] + arr1[i]) {
				minIdx = i;
				minSum = arr2[index[i]] + arr1[i];
			}
		}
		output.push_back(vector<int>{arr1[minIdx], arr2[index[minIdx]]});
		++index[minIdx];
		--k;
	}
	return output;
}


int main() {
	int n1{}, n2{};
	cin >> n1 >> n2;

	int* arr1 = new int[n1], *arr2 = new int[n2];

	for (int i = 0; i < n1; i++) {
		cin >> arr1[i];
	}

	for (int i = 0; i < n2; i++) {
		cin >> arr2[i];
	}

	int k{};
	cin >> k;

	vector<vector<int>> output = pairs(arr1, n1, arr2, n2, k);
	for (auto p: output) {
		cout << "(" << p.at(0) << ", " << p.at(1) << ")" << endl;
	}
	delete [] arr1;
	delete [] arr2;
	return 0;
}