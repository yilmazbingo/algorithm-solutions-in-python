DIRECTIONS = [
  [-2, -1],
  [-2, 1],
  [-1, 2],
  [1, 2],
  [2, 1],
  [2, -1],
  [1, -2],
  [-1, -2],
];
def knight_probability(size,moves,col,row):
    if row<0 or row>=size or col<0 or col>=size:
        return 0
    if moves==0:
        return 1
    res=0
    for dir in DIRECTIONS:
        res+=knight_probability(size,moves-1,row+dir[0],col+dir[1])/8
    return res
print(knight_probability(8, 2, 4, 4))
# T:O(8^moves) S: O(8^moves)

def memoized(size, moves, row, col):
    dp = [[[None] * size for i in [0] * size] for i in [0] * (moves + 1)]
    print(len(dp))
    return recurse(size, moves, row, col, dp)


def recurse(size, moves, row, col, dp):
    if row < 0 or row >= size or col < 0 or col >= size:
        return 0
    if moves == 0:
        return 1
    if dp[moves][row][col] != None:
        return dp[moves][row][col]
    res = 0
    for dir in DIRECTIONS:
        res += recurse(size, moves - 1, row + dir[0], col + dir[1], dp) / 8
    dp[moves][row][col] = res
    return dp[moves][row][col]


print(memoized(8, 2, 3, 3))
