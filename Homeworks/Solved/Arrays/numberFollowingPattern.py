'''
If I, then number should increase
if D, then number should decrease

eg:
	I -> 12
	II -> 123
	D -> 21
	DD -> 321
	DID -> 2143

'''

def numberPattern(string: str) -> str:
	result, res = str(), list()
	minSoFar, positionOfI = 0, 0
	if string[0] == 'I':
		positionOfI = 1
		res.extend([1, 2])
	else:
		positionOfI = 0
		res.extend([2, 1])
	minSoFar = 3

	for i in range(1, len(string)):
		if string[i] == 'I':
			res.append(minSoFar)
			positionOfI = i + 1
		else:
			res.append(res[i])
			for j in range(positionOfI, i + 1):
				res[j] += 1

		minSoFar += 1

	result = ''.join(map(str, res))
	return result


print(numberPattern(input()))


