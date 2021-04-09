#include <iostream>
using namespace std;

int rainWater(int array[], int size) {
	int water{};
	int leftMax[size], rightMax[size];
	leftMax[0] = array[0];
	rightMax[size - 1] = array[size - 1];

	for (int i = 1; i < size; ++i) {
		leftMax[i] = max(leftMax[i - 1], array[0]);
		rightMax[size - i - 1] = max(rightMax[size - i], array[size - i - 1]);
	}

	for (int i = 0; i < size; ++i) {
		int minHeight = min(leftMax[i], rightMax[i]);
		if (minHeight > array[i]) {
			water += minHeight - array[i];
		}
	}
	return water;
}


int main() {
	int n{};
	cin >> n;
	int* heights = new int[n];
	for (unsigned int i = 0; i < n; ++i) {
		cin >> *(heights + i);
	}

	cout << rainWater(heights, n) << endl;
	delete [] heights;
	return 0;
}