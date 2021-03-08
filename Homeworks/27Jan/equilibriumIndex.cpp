/*
Given an array A of N positive numbers. The task is to find the first 
Equilibium Point in the array. Equilibrium Point in an array is a position 
such that the sum of elements before it is equal to the sum of elements after it.

Example 1:

Input:
N = 1
A[] = {1}
Output: 1
Explanation: Since its the only 
element hence its the only equilibrium 
point. 
Example 2:

Input:
N = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case 
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2).
*/

/*


*/





#include <iostream>
using namespace std;


int equilibriumPoint(long long int a[], int n) {
    if (n == 1) {
        return n;
    }
    long long int rightSum{};
    for (int i = 0; i < n; ++i) {
        rightSum += a[i];
    }

    long long int leftSum{};
    for (int i = 0; i < n; ++i) {
        rightSum -= a[i];
        if (rightSum == leftSum) {
            return i + 1;
        }
        leftSum += a[i];
    }
    return -1;
}