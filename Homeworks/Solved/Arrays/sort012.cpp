/*
Sort 0, 1, and 2 such that 0s are followed by 1s followed by 2s.

*/

#include <iostream>
#include <algorithm>
using namespace std;

void printArray(const int* array, int n) {
	for (int i = 0; i < n; i++) {
		cout << *(array + i) << " ";
	}
	// array[0] = 10;
}



int main() {
	int n{};
	cin >> n;
	int* array = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> array[i];
	}

	printArray(array, n);
	cout << endl << endl;

	int l{}, mid{}, h{n - 1};
	while (mid <= h) {
		if (array[mid] == 0) {
			swap(array[l++], array[mid++]);
		} else if (array[mid] == 1) {
			++mid;
		} else {
			swap(array[mid], array[h--]);
		}
	}
	printArray(array, n);
	cout << endl;
	delete [] array;
	return 0;
}