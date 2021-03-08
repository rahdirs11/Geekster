/*
Given an unsorted array of nonnegative integers, 
find a continuous subarray which adds to a given number.
*/

/*
APPROACH:
-> use two pointer method
-> left and right will be at 0th index and 1st index respectively
-> find sum by adding left and right
-> increment right if sum <= required sum
-> decrement sum by subtracting arr[left] and increment left
*/
#include <iostream>
#include <vector>
using namespace std;

vector<int> subarraySum(int arr[], int n, int s) {
    int left{}, right{1}, currSum{arr[0]};
    while (right <= n) {
        while (currSum > s && left < right - 1) {
            currSum -= arr[left];
            ++left;
        }
        if (currSum == s) {
            return vector<int>{left + 1, right};
        }
        if (right < n) {
            currSum += arr[right];
        }
        ++right;
    }
    return vector<int>{-1};
}

int main() {
    int n{}, s{};
    vector<int> output;
    cin >> n >> s;
    int *a = new int[n];
    for (int i = 0; i < n; ++i) {
        cin >> *(a + i);
    }
    output = subarraySum(a, n, s);
    for (auto o: output) {
        cout << o << " ";
    }
    cout << endl;
    delete [] a;
    return 0;
}
