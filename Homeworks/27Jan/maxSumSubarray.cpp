/*Kadanes Algorithm*/

#include <iostream>

int maxSubarraySum(int a[], int n) {
    int currSum{}, maxSum = INT_MIN;
    for (int i = 0; i < n; ++i) {
        currSum += a[i];
        if (currSum > maxSum) maxSum = currSum;
        if (currSum < 0) currSum = 0;
    }
    return maxSum;
}