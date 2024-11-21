board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

length = len(board)

"""
Tervek: 
tábla megjelenítése
"""

def show(table):
	for row in table:
		for e in row:
			print(e, end='  ')
		print('')

def solve(table):
	next_empty = find_blanks(board)
	if not next_empty:
		return True
	else:
		row, col = next_empty
		for i in range(1, 10):
			if check_valid(board, i, row, col):
				board[row][col] = i
				if solve(board):
					return True
				board[row][col] = 0
	return False

def find_blanks(table):
	for i in range(length):
		for j in range(length):
			if table[i][j] == 0:
				return (i,j)
	return None


def check_valid(table, num, x, y):
	for e in table[x]:
		if e == num:
			return False
	for i in range(length):
		if table[i][y] == num:
			return False

	secX = x // 3
	secY = y // 3

	for i in range(secX*3, secX*3+3):
		for j in range(secY*3, secY*3+3):
			if table[i][j] == num:
				return False
	return True


solve(board)
show(board)