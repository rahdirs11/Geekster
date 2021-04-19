#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n{};
	cin >> n;

	int* array = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> array[i];
	}

	int lowVal{}, highVal{};
	cin >> lowVal >> highVal;

	int l{}, mid{}, h{n - 1};
	while (mid <= h) {
		if (array[mid] < lowVal) {
			swap(array[mid++], array[l++]);
		} else if (array[mid] >= lowVal && array[mid] <= highVal) {
			++mid;
		} else {
			swap(array[mid], array[h--]);
		}
	}

	for (int i = 0; i < n; ++i) {
		cout << array[i] << " ";
	}
	cout << endl;
	delete [] array;
	return 0;
}