#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n{};
	cin >> n;
	int* array = new int[n];
	int i{-1};
	for (int x = 0; x < n; ++x) {
		cin >> array[x];
	}

	for (int j = 0; j < n; j++) {
		if (array[j] < 0) {
			swap(array[j], array[++i]);
		}
	}

	int neg{}, pos{i + 1};
	while (neg < pos && array[neg] < 0 && pos < n) {
		swap(array[neg], array[pos]);
		neg += 2;
		++pos;
	}

	for (int x = 0; x < n; x++) {	
		cout << array[x] << " ";
	}
	delete [] array;
	return 0;
}