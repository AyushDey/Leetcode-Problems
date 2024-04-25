# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
import collections


def validSudoku(board):
    col = collections.defaultdict(set)
    row = collections.defaultdict(set)
    # Checking the 3x3 matrices by indexing by (r//3, c//3)
    squares = collections.defaultdict(set) 

    for r in range(9):
        for c in range(9):
            # Skip empty cells
            if board[r][c] == ".":
                continue
            # Check if current number exists in 
            # corresponding row/col/square
            if (
                board[r][c] in row[r]
                or board[r][c] in col[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                # If duplicate found, board is invalid
                return False
            # Add current number to row/col/square sets
            col[c].add(board[r][c])
            row[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(validSudoku(board))
