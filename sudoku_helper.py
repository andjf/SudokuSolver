def solve(board):
	for y in range(len(board)):
		for x in range(len(board[y])):
			if board[y][x] == 0:
				for number in range(1, len(board) + 1):
					if possible(board, x, y, number):
						board[y][x] = number
						if solve(board) != -1:
							return board
						board[y][x] = 0
				return -1
	return board

def possible(board, x, y, num):
	if not(number_in_row(board, num, y)):
		if not(number_in_column(board, num, x)):
			if not(number_in_box(board, num, x // 3, y // 3)):
				return True

def number_in_box(board, num, cell_x, cell_y):
	for x in range(3):
		for y in range(3):
			if board[cell_y * 3 + y][cell_x * 3 + x] == num:
				return True

def number_in_column(board, num, column):
	for row in board:
		if row[column] == num:
			return True

def number_in_row(board, num, row):
	return num in board[row]