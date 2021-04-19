#include <iostream>
#include <algorithm>
using namespace std;

void printArray(const int array[], int n) {
	for (int i = 0; i < n; ++i) {
		cout << array[i] << " ";
	}
}


int main() {
	int n{};
	cin >> n;	// size of array
	int* array = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> array[i];
	}
	cout << "Before process =>" << endl;
	printArray(array, n);
	cout << endl << endl;

	int idx{-1};
	for (int j = 0; j < n; ++j) {
		if (array[j] != 0) {
			swap(array[j], array[++idx]);
		}
	}

	cout << "After process =>" << endl;
	printArray(array, n);
	cout << endl;
	delete [] array;
	return 0;
}