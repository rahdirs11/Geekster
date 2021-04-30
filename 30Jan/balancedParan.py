def balanced(string, answer, length, l: set, openB=0, closeB=0):
	if len(string) == 0:
		# print(answer)
		l.add(answer)
		return

	if closeB > openB or openB > length // 2:
		return


	remaining = string[1: ]
	current = string[0]
	balanced(remaining, answer + current, length, l, openB + 1, closeB) if current == '(' else balanced(remaining, answer + current, length, l, openB, closeB + 1)
	balanced(remaining, answer, length, l, openB, closeB)


l = set()
balanced('()())()', "", 7, l)
maxLen = 0

for i in l:
	maxLen = max(len(i), maxLen)


for i in l:
	if len(i) == maxLen:
		print(i)
