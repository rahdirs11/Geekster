#include <iostream>
using namespace std;

int binarySearch(int array[], int low, int high, int key) {
	while (low <= high) {
		int mid = low + ((high - low) >> 1);
		if (array[mid] == key) {
			return mid;
		} else if (array[mid] < key) {
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}
	return -1;
}



int findRotatedIdx(int array[], int high, int low) {
	if (high < low) {
		return -1;
	}
	if (high == low) {
		return high;
	}

	int mid = low + ((high - low) >> 1);
	if (mid < high && array[mid] > array[mid + 1]) {
		return mid;
	} 

	if (mid > low && array[mid] < array[mid - 1]) {
		return mid - 1;
	}

	if (array[low] >= array[mid]) {
		return findRotatedIdx(array, mid - 1, low);
	}

	return findRotatedIdx(array, high, mid + 1);
}


int main() {
	int n{};
	// cout << "Enter size of array:\t";
	cin >> n;
	int* array = new int[n];
	// cout << "Enter " << n << " elements:\t";
	for (int i = 0; i < n; ++i) {
		cin >> array[i];
	}
	// cout << "\n\nElements:\n";
	// for (int i = 0; i < n; ++i) {
	// 	cout << array[i] << " ";
	// }
	// cout << endl;
	// cout << "Enter key element to be searched in array:\t";
	int key{};
	cin >> key;

	int rotatedIndex = findRotatedIdx(array, n - 1, 0);
	// cout << rotatedIndex << endl;
	int elementIdx = rotatedIndex == -1? binarySearch(array, 0, n - 1, key): (array[rotatedIndex] == key? rotatedIndex: (array[0] > key? binarySearch(array, rotatedIndex + 1, n - 1, key): binarySearch(array, 0, rotatedIndex - 1, key)));
	// cout << elementIdx << endl;
	if (elementIdx == -1) {
		cout << "Element not found";
	} else {
		cout << "Element found at index " << elementIdx;
	}
	cout << endl;
	delete [] array;
	return 0;
}