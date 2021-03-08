#include <iostream>
using namespace std;

int utopianTree(int n=0);

int main() {
	int n{};
	cin >> n;
	cout << utopianTree(n) << endl;
	return 0;
}

int utopianTree(int n) {
	if (n == 0)
		return 1;
	int i{1}, height{1};
	while (i <= n) {
		if (i % 2 == 1) {
			height *= 2;
		} else {
			++height;
		}
		++i;
	}
	return height;
}
