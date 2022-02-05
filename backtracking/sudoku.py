from typing import List
'''
Time complexity: O(9^(n*n)). 
For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)). The time complexity remains the same but there will be some early pruning so the time taken will be much less than the naive algorithm but the upper bound time complexity remains the same.
Since we are pruning (9!)^9
Space Complexity: O(n*n). 
To store the output array a matrix is needed.
'''
'''
recursive backtracking is a brute force solution. we are still performing brute force solution. in the worst case we receive empty board state. that means we have 81 cells to fill. 
for each cell we have 9 iterations to try. for next one we have 9. 9^81
'''

def get_box_id(row, col):
    row_val = (row // 3) * 3
    col_val = (col // 3)
    return col_val + row_val

def is_valid(box, row, col, num):
    if num in box or num in row or num in col:
        return False
    else:
        return True

def backtrack(board, boxes, rows, cols, r, c):
    if r >= len(board) or c >= len(board[0]):
        return True

    if board[r][c] == ".":
        for num in range(1, 10):
            box_id = get_box_id(r, c)
            box = boxes[box_id]
            row = rows[r]
            col = cols[c]
            str_num = str(num)
            board[r][c] = str_num
            if is_valid(box, row, col, str_num):
                boxes[box_id][str_num] = True
                rows[r][str_num] = True
                cols[c][str_num] = True
                if c == len(board[0]) - 1:
                    if backtrack(board, boxes, rows, cols, r + 1, 0):
                        return True
                else:
                    if backtrack(board, boxes, rows, cols, r, c + 1):
                        return True
                del box[str_num]
                del row[str_num]
                del col[str_num]
            board[r][c] = "."
    else:
        if c == len(board[0]) - 1:
            if backtrack(board, boxes, rows, cols, r + 1, 0):
                return True
        else:
            if backtrack(board, boxes, rows, cols, r, c + 1):
                return True

    return False


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows = [{} for i in range(n)]
        cols = [{} for i in range(n)]
        boxes = [{} for i in range(n)]
        for r in range(n):
            for c in range(n):
                if board[r][c] != ".":
                    val = board[r][c]
                    box_id = get_box_id(r, c)
                    boxes[box_id][val] = True
                    rows[r][val] = True
                    cols[c][val] = True
        # so far i get the state of the board
        backtrack(board, boxes, rows, cols, 0, 0)


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


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        boxes = [{}] * n
        rows = [{}] * n
        cols = [{}] * n
        for r in range(n):
            for c in range(n):
                if board[r][c] != ".":
                    val = board[r][c]
                    box_id = get_box_id(r, c)
                    boxes[box_id][val] = True
                    rows[r][val] = True
                    cols[c][val] = True

        backtrack(board, boxes, rows, cols, 0, 0)


s = Solution()
s.solveSudoku(board)
print(board)