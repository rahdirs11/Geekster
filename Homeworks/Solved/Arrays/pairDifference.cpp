#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;


pair<int, int> findDifference(int arr[], int n, int difference) {
	int l{}, r{1};
	while (l < n && r < n) {
		int diff = arr[r] - arr[l];
		if (r != l && diff == difference) {
			return pair<int, int>{arr[l], arr[r]};
		} else if (diff > difference) {
			++l;
		} else {
			++r;
		}
	}
	return pair<int, int>{-1, -1};
}


int main() {
	int n{};
	cin >> n;
	int* array = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> *(array + i);
	}

	int diff{};
	cin >> diff;
	sort(array, array + n);

	pair<int, int> output = findDifference(array, n, diff);
	if (output.first == -1) {
		cout << "(-1, -1)";
	} else {
		cout << "(" << output.first << ", " << output.second << ")";
	}
	cout << endl;
	delete [] array;
	return 0;
}