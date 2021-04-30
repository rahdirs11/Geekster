#include <iostream>
using namespace std;

int minSwaps(int arr[], int n, int k) {
	int good{}, bad{};
	for (int i = 0; i < n; i++) {
		good += arr[i] <= k? 1: 0;
	}

	for (int i = 0; i < good; ++i) {
		bad += arr[i] > k? 1: 0;
	}

	int res{bad};

	for (int i = 0, j = good; j < n; ++i, ++j) {
		if (arr[i] > k) {
			--bad;
		}

		if (arr[j] > k) {
			++bad;
		}

		res = min(res, bad);
	}
	return res;
}


int main() {
	int n{};
	cin >> n;

	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];		
	}

	int k{};
	cin >> k;

	cout << minSwaps(arr, n, k);

	delete [] arr;
	return 0;
}

/*

k = 3
arr = {5, 6, 3, 1, 2};

good = 3
bad = 2




*/