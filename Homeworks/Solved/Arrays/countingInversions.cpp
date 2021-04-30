#include <iostream>
using namespace std;

int mergeSort(int arr[], int n) {
	int temp[n]{0};
	return mergeSort2(arr, temp, 0, n - 1);
}



int merge(int arr[], int temp[], int left, int mid, int right) {
	int i{left}, k{left}, j{mid + 1};
	int inversions{};

	while (i <= mid && j <= right) {
		if (arr[i] <= arr[j]) {
			temp[k] = arr[i++];
		} else {
			temp[k] = arr[j++];
			inversion += mid - i + 1;
		}
		++k;
	}

	for (int i = left; i <= right; ++i) {
		arr[i] = temp[i];
	}

	return inversion;
}


int mergeSort2(int arr[], int temp[], int left, int right) {
	int inversions{};
	if (left < right) {
		inversions += mergeSort2(arr, temp, left, mid);
		inversions += mergeSort2(arr, temp, mid + 1, right);

		inversions += merge(arr, temp, left, mid, right);
	}
	return inversions;
}