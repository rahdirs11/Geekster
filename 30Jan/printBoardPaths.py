def paths(row: int, col: int, cr: int=0, cc: int=0):
	if row == cr and col == cc:
		return ['']

	if row < cr or col < cc:
		return []
	# horizontal movement
	result = []
	recResH = paths(row, col, cr, cc + 1)
	for r in recResH:
		result.append(f'H{r}')

	# vertical movement
	recResV = paths(row, col, cr + 1, cc)
	for r in recResV:
		result.append(f'V{r}')

	return result


def pathsQA(row, col, answer, cr: int=0, cc: int=0):
	if col == cc and row == cr:
		print(answer)
		return


	# horizontal movement
	for i in range(1, col + 1):
		if not cc + i > col:
			pathsQA(row, col, f'H{i} {answer}', cr, cc + i)

	# vertical movement
	for i in range(1, row + 1):
		if not cr + i > row:
			pathsQA(row, col, f'V{i} {answer}', cr + i, cc)


pathsQA(2, 2, '')




# for path in paths(3, 3):
# 	print(path)