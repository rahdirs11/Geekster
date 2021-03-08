/*Given an array of DISTINCT elements, rearrange the elements of array in zig-zag fashion in O(n) time. The converted array should be in form a < b > c < d > e < f. 
Example:

Input: arr[] = {4, 3, 7, 8, 6, 2, 1} 
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

Input: arr[] = {1, 4, 3, 2} 
Output: arr[] = {1, 4, 2, 3}
*/
#include <iostream>
using namespace std;

void zigzag(int a[], int n) {
    bool less = true;
    for (int i = 0; i < n - 1; ++i) {
        if (less) {
            if (a[i] > a[i + 1]) {
                a[i] *= a[i + 1];
                a[i + 1] = a[i] / a[i + 1];
                a[i] /= a[i + 1];
            } // swapping
        } else {
            if (a[i] < a[i + 1]) {
                a[i] *= a[i + 1];
                a[i + 1] = a[i] / a[i + 1];
                a[i] /= a[i + 1];   
            }
        }
        less = !less;
    }
    for (int i = 0; i < n; ++i) {
        cout << a[i] << " ";
    }
}

int main() {
    int n{};
    cin >> n;
    int *a = new int[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    zigzag(a, n);
    delete [] a;
    return 0;
}