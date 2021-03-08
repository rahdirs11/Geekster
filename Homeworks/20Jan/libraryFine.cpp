#include <iostream>
using namespace std;

int libraryFine(int d1, int m1, int y1, int d2, int m2, int y2) {
	if (y1 > y2) {
		return 10000;
	} else {
		if (m1 > m2) {
			return (m1 - m2) * 500;
		} else {
			return (d1 > d2)? (15 * (d1 - d2)): 0;
		}
	}
}

int main() {
	int d1{}, m1{}, y1{}, d2{}, m2{}, y2{};
	cin >> d1 >> m1 >> y1;
	cin >> d2 >> m2 >> y2;
	cout << libraryFine(d1, m1, y1, d2, m2, y2) << endl;
	return 0;
}

