#include <iostream>
// #include <algorithm>
using namespace std;


void swap(int &arr[], int l, int r) {
	arr[l] = arr[l] ^ arr[r];
	arr[r] = arr[l] ^ arr[r];
	arr[l] = arr[l] ^ arr[r];
}


int main() {
	int n{};
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> *(arr + i);
	}

	int flag = true;
	for (int i = 0; i + 1 < n; ++i) {
		if (flag) {
			if (arr[i] > arr[i + 1]) {
				swap(arr[i], arr[i + 1]);
			}
			flag = !flag;
		} else {
			if (arr[i] < arr[i + 1]) {
				swap(arr[i], arr[i + 1]);
			}
			flag = !flag;
		}
	}

	for (int i = 0; i < n; ++i) {
		cout << arr[i] << " ";
	}
	cout << endl;
	delete [] arr;
	return 0;
}