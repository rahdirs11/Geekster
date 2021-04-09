#include <iostream>
#define N 100
using namespace std;

void printMatrix(int a[][N], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) 
			cout << a[i][j] << " ";
		cout << endl;
	}
}


void rotateMatrix(int a[][N], int n) {
	for (int i = 0; i < n / 2; ++i) {
		for (int j = i; j < n - i - 1; ++j) {
			int temp = a[j][n - i - 1];
			a[j][n - i - 1] = a[n - i - 1][n - j - 1];
			a[n - i - 1][n - j - 1] = a[n - j - 1][i];
			a[n - j - 1][i] = a[i][j];
			a[i][j] = temp;
		}
	}
}


int main() {
	int n{};
	cin >> n;
	int a[n][N];
	for (int i = 0; i < n; i++) {
		// *a = new int[n];
		for (int j = 0; j < n; j++) 
			cin >> a[i][j];
	}

	printMatrix(a, n);
	rotateMatrix(a, n);
	printMatrix(a, n);
	return 0;
}