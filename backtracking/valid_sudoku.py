
import math
import collections
from typing import List
def get_box_id(row ,col):
    # math.floor returns float but list indices have to be int
    row_val =int(math.floor(row//3 ) *3)
    col_val =int(math.floor(col//3))
    return col_val +row_val
class Solution:
    def faster(self, board:List[List[int]])->bool:
        n = len(board)
        boxes = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val != ".":
                    if (val in rows[r]) or (val in cols[c]) or (val in boxes[(r // 3, c // 3)]):
                        return False
                    else:
                        cols[c].add(val)
                        rows[r].add(val)
                        boxes[(r // 3, c // 3)].add(val)
        return True
    def isValidSudoku(self, board:List[List[int]])->bool:
        #------------- THIS WAS CAUSIN ERROR
        # boxes=[{}]*n
        # rows=[{}]*n    -
        # cols=[{}]*n    -
        #-------------
        n = len(board)
        boxes=[{} for i in range(n)]
        rows=[{}for i in range(n)]
        cols=[{} for i in range ( n)]
        for r in range(n):
            for c in range(n):
                val=board[r][c]
                box_id=get_box_id(r,c)

                if val!=".":
                    if (val not in rows[r]) and (val not in cols[c])and (val not in boxes[box_id]):
                        rows[r][val]=True
                        cols[c][val]=True
                        boxes[box_id][val]=True
                    else:
                        return False
        return True
board=[["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]
s=Solution()
print(s.isValidSudoku(board))
print(s.faster(board))


# import math
#
#
# def get_box_id(row, col):
#     # math.floor returns float but list indices have to be int
#     row_val = int(math.floor(row // 3) * 3)
#     col_val = int(math.floor(col // 3))
#     return col_val + row_val


# class Solution(object):
#     def faster(self, board):
#
#         n = len(board)
#         # boxes=[{}]*n
#         # rows=[{}]*n
#         # cols=[{}]*n
#         boxes = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#
#         cols = collections.defaultdict(set)
#         for r in range(n):
#             for c in range(n):
#                 val = board[r][c]
#
#                 if val != ".":
#                     if (val in rows[r]) or (val in cols[c]) or (val in boxes[(r // 3, c // 3)]):
#                         return False
#                     else:
#                         cols[c].add(val)
#                         rows[r].add(val)
#                         boxes[(r // 3, c // 3)].add(val)
#         return True
#     def isValidSudoku(self, board):
#
#         n = len(board)
#         # boxes=[{}]*n
#         # rows=[{}]*n
#         # cols=[{}]*n
#         boxes = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#
#         cols = collections.defaultdict(set)
#         for r in range(n):
#             for c in range(n):
#                 val = board[r][c]
#                 box_id = get_box_id(r, c)
#
#                 if val != ".":
#                     if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_id]):
#                         return False
#                     else:
#                         cols[c].add(val)
#                         rows[r].add(val)
#                         boxes[box_id].add(val)
#         return True
