'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Find the number of good pairs.

Input Format

first line contain N, no of elements in nums arrays. Second line contain Array elements

Constraints

1<=N<=1000 1<=Ai<=1000

Output Format

Print desired output

Sample Input 0

6
1 2 3 1 1 3
Sample Output 0

4
'''
from typing import List
def goodPairs(array: List[int]) -> int:
	pairs = 0
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			if array[i] == array[j]:
				pairs += 1
	return pairs


if __name__ == '__main__':
	n = int(input())
	array = [int(x) for x in input().split()]

	print(goodPairs(array))