def findElement(arr: list) -> int:
	xor = int()
	for x in arr:
		xor ^= x
	return xor

print(findElement(list(map(int, input().split()))))