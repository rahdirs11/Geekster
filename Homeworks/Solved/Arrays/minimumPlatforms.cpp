/*
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, 
same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms,
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int n{};
	cin >> n;
	int* arr = new int[n], dep = new int[n];
	for (int i = 0; i < n; i++)	{
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++)	{
		cin >> dep[i];
	}

	sort(arr, arr + n);
	sort(dep, dep + n);
	int maxPlatform{}, currPlatform{1};
	int i{1}, j{};
	while (i < n && j < n) {
		if (dep[j] > arr[i]) {
			--currPlatform;
			++j;
		} else {
			++currPlatform;
			++i;
		}

		maxPlatform = max(maxPlatform, currPlatform);
	}

	cout << maxPlatform << endl;
	delete [] arr;
	delete [] dep;
	return 0;
}