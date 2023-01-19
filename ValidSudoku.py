from collections import defaultdict

def suduko(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    square = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            if board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in square[(i // 3, j // 3)]:
                return False
            cols[j].add(board[i][j])
            rows[i].add(board[i][j])
            square[i // 3, j // 3].add(board[i][j])

    return True

board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(suduko(board))