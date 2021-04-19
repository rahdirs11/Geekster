#include <iostream>
using namespace std;


bool hasPairSum(int a[], int l, int r, int n, int target) {
	while (l != r) {
		if (a[l] + a[r] == target) {
			return 1;
		} else if (a[l] + a[r] < target) {
			l = (l + 1) % n;
		} else {
			r = (n + r - 1) % n;
		}
	}
	return 0;
}



int findPivot(int a[], int l, int h) {
	if (h < l) {
		return -1;
	}
	if (l == h) {
		return l;
	}
	int mid = l + ((h - l) >> 1);
	if (mid < h && a[mid] > a[mid + 1]) {
		return mid;
	}
	if (mid > l && a[mid] < a[mid - 1]) {
		return mid - 1;
	}
	if (a[l] >= a[mid]) {
		return findPivot(a, l, mid - 1);
	}
	return findPivot(a, mid + 1, h);
}



int main() {
	int n{};
	cin >> n;
	int* a = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	int target{};
	cin >> target;
	int rotatedIdx = findPivot(a, 0, n - 1);
	if (rotatedIdx == -1) {
		// regular 
		cout << hasPairSum(a, 0, n - 1, n, target);
	} else {
		cout << hasPairSum(a, rotatedIdx + 1, rotatedIdx, n, target);
	}
	cout << endl;
	delete [] a;
	return 0;
}