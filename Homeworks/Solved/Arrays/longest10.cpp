#include <iostream>
#include <unordered_map>
using namespace std;


int main() {
	int n{};
	cin >> n;
	int* arr = new int[n];
	unordered_map<int, int> map;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
		if (arr[i] == 0) {
			arr[i] = -1;
		}
	}


	int maxLen = 0, sum = 0, lastIndex = 0;

	for (int i = 0; i < n; ++i) {
		sum += arr[i];
		if (sum == 0) {
			maxLen = i + 1;
			lastIndex = i;
		}

		if (map.find(sum) != map.end()) {
			if (maxLen < i - map[sum]) {
				maxLen = i - map[sum];
				lastIndex = i;
			}
		} else {
			map[sum] = i;
		}
	}

	cout << (lastIndex - maxLen  + 1) << " to " << lastIndex << endl;

	delete [] arr;
	return 0;
}