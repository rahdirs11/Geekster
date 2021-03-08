def printArray(arr: list):
	for j in range(len(arr[0])):
		if j % 2:
			for i in range(len(arr) - 1, -1, -1):
				print(arr[i][j], e)

printArray([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])