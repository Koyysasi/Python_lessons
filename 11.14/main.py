table = [
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
LENGHT = len(table[0])
def print_board(board):
    for row in board:
        for e in row:
            print(e, end=" ")
        print("")

def solve(board) -> bool:
    next_empty = find_empty(board)
    if not next_empty:
        return True
    else:
        row, col = next_empty
        for i in range(1,10):
            if is_valid(board, i, row, col):
                board[row][col] = i
                if solve(board):
                    return True
                board[row][col] = 0
        return False

def find_empty(board) -> tuple[int,int] | None:
    for i in range(LENGHT):
        for j in range(LENGHT):
            if board[i][j] == 0:
                return (i,j)
    return None

def is_valid(board, num, row, col) -> bool:
    # Sor ellenőrzése
    for e in board[row]:
        if e == num: 
            return False
    
    # Oszlop ellenőrzése
    for i in range(LENGHT):
        if board[i][col] == num:
            return False

    # Részmátrix ellenőrzés
    sec_row = row // 3
    sec_lol = col // 3
    for i in range(3*sec_row,3*sec_row + 3):
        for j in range(3*sec_lol,3*sec_lol + 3):
            if board[i][j] == num:
                return False
    return True 


print_board(table)
print("---------------------------------")
solve(table)
print_board(table)