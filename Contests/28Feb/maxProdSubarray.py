'''Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Note: According to testcases answer will not overflow long

Input Format

First line contain N, number of elements in an array. Second line contain array elements.

Constraints

1<=N<=100000
-100<=Ai<=100
Output Format

Print desired output

Sample Input 0

4
2 3 -2 4 
Sample Output 0

6'''
from typing import List
import sys

def maxProdSubarray(array: List[int]) -> int:
	maxProd, prod = -sys.maxsize - 1, 1
	for i in array:
		prod *= i
		maxProd = max(prod, maxProd)
		if prod <= 0:
			prod = 1

	return maxProd


if __name__ == '__main__':
	n = int(input())
	array = list(map(int, input().split()))

	print(maxProdSubarray(array))