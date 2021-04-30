def isSafe(board, row, col, k):
	for i in range(row + 1):
		if board[i][col] == k:
			return False

	for i in range(col + 1):
		if board[row][i] == k:
			return False

	from math import sqrt
	box = int(sqrt(len(board)))
	startBoxRow, startBoxCol = row - row % box, col - col % box
	for i in range(startBoxRow, startBoxRow + box):
		for j in range(startBoxCol, startBoxCol + box):
			if board[i][j] == k:
				return False

	return True


def solveSudoku(board):
	row, col, filled = -1, -1, True
	for i in range(len(board)):
		for j in range(len(board[0])):
			# if we find an empty box, it means sudoku is incomplete, and we have to start filling elements in that spot
			if board[i][j] == 0:
				filled = not filled
				row, col = i, j
				break
		if not filled:
			break

	# if we didnt find any empty box, it means the board is filled and we have a solution, so we print and return true
	if filled:
		for row in range(len(board)):
			for col in range(len(board[0])):
				print(board[row][col], end=" | ")
			print()
			print('-'*35)
		return True

	# trying to fill a box with values from 1 to 9
	for i in range(1, 10):
		if isSafe(board, row, col, i):
			board[row][col] = i
			if solveSudoku(board):
				return True
			# if we cant fill, then we backtrack and unset that value to start all over from that box
			else:
				board[row][col] = 0

	return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if not solveSudoku(grid):
	print("No Solution!")
