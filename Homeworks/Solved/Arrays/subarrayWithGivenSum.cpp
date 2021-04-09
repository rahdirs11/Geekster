#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> subarraySum(int arr[], int n, int s) {
		int l{};
		int sum = arr[l];
		for (int i = 1; i <= n; ++i) {
			while (sum > s && l < i - 1) {
				sum -= arr[l++];
			}

			if (sum == s) {
				return vector<int>{l + 1, i};
			}

			if (i < n) {
				sum += arr[i];
			}
		}
		return vector<int>{-1};
	}
};

int main() {
	Solution s;
	int n{};
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	int sum{};
	cin >> sum;
	for (auto i: s.subarraySum(arr, n, sum)) {
		cout << i << " ";
	}
	cout << endl;
	delete [] arr;
	return 0;
}