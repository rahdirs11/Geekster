#include <iostream>	
#include <algorithm>
using namespace	std;	

int main() {
	int n{};
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}

	int r{n}, l{n - 1};
	while (l >= 0) {
		if (arr[l] == 1) {
			--r;
			swap(arr[l], arr[r]);
		}
		--l;
	}

	for (int i = 0; i < n; ++i) {
		cout << arr[i] << " ";
	}
	cout << endl;
	delete [] arr;
	return 0;
}


/*

1 0 1 1 1

*/