def findRepeated(arr: list) -> int:
	i = 0
	while i < len(arr):
		if arr[abs(arr[i]) - 1] < 0:
			return abs(arr[i])

		arr[abs(arr[i]) - 1]  *= (-1)
		i += 1

	print(' '.join(map(str, arr)))
	return -1


print(findRepeated([int(x) for x in input().split()]))