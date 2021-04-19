#include <iostream>
using namespace std;

void printArray(const int array[], int n, int idx=0) {
	if (idx == n) {
		return;
	}

	cout << array[idx] << " ";
	printArray(array, n, idx + 1);
}


int main() {
	int n{};
	cin >> n;	// size of array

	int* arr = new int[n];
	int* left = new int[n];
	int* right = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
		if (i == 0) {
			left[i] = 0;
		} else {
			if (arr[i] >= arr[i - 1]) {
				left[i] = left[i - 1] + 1;
			} else {
				left[i] = 0;
			}
		}
	}
	right[n - 1] = 0;
	for (int i = n - 2; i >= 0; --i) {
		if (arr[i] >= arr[i + 1]) {
			right[i] = right[i + 1] + 1;
		} else {
			right[i] = 0;
		}
	}

	// cout << "Array:\n";
	// printArray(arr, n);

	// cout << endl << endl << "Left:\n";
	// printArray(left, n);

	// cout << endl << endl << "Right:\n";
	// printArray(right, n);

	int maxLen{}, currLen{};
	for (int i = 0; i < n; ++i) {
		currLen = left[i] + right[i];
		maxLen = maxLen < currLen? currLen: maxLen;
	}

	cout << (maxLen + 1) << endl;
	delete [] arr, left, right;
	return 0;
}