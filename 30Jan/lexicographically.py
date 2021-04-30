def lex(value: int, limit: int):
	print(value, end=" ")

	for i in range(10):
		if value * 10 + i <= limit:
			lex(value * 10 + i, limit)		

	if value < 9:
		print()
		lex(value + 1, limit)


lex(1, 1000)