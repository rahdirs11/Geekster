def printFirstOccurrence(string: str) -> str:
	output = str()
	for s in string:
		if s not in output:
			output += s

	return output


if __name__ == '__main__':
	for _ in range(int(input())):
		print(printFirstOccurrence(input()))