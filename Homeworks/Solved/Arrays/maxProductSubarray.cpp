#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int* array = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> array[i];
	}

	int maxSoFar{}, minEndingHere{1}, maxEndingHere{1};
	int flag{};
	for (int i = 0; i < n; ++i) {
		if (array[i] == 0) {
			maxEndingHere = minEndingHere = 1;
		} else if (array[i] < 0) {
			int temp{maxEndingHere};
			maxEndingHere = max(1, array[i] * minEndingHere);
			minEndingHere = temp * array[i];
		} else {
			flag = 1;
			maxEndingHere *= array[i];
			minEndingHere = min(1, array[i] * minEndingHere);
		}

		maxSoFar = max(maxSoFar, maxEndingHere);
	}

	cout << maxSoFar;
	cout << endl; 
	delete [] array;
	return 0;
}