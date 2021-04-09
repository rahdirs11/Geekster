#include <iostream>
#include <unordered_map>
using namespace std;


int longestSubarrayDivByK(int arr[], int n, int k) {
	int* modArr = new int[n];
	int sum{};
	for (int i = 0; i < n; ++i) {
		sum += arr[i];
		modArr[i] = ((sum % k) + k) % k;
	}
	int maxLen{}, idx{};
	unordered_map<int, int> map;
	for (int i = 0; i < n; ++i) {
		if (modArr[i] == 0) {
			maxLen = i + 1;
		} else if (map.find(modArr[i]) == map.end()) {
			map[modArr[i]] = i;
		} else {
			maxLen = max(maxLen, i - map[modArr[i]]);
		}
	}
	return maxLen;
}



int main() {
	int n{}, k{};
	cin >> n >> k;

	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}


	int output = longestSubarrayDivByK(arr, n, k);
	cout << output << endl;
	delete [] arr;
	return 0;
}