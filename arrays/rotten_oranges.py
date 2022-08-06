'''
994. Rotting Oranges  Medium
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh_oranges += 1
        current_queue_size = len(queue)
        minutes = 0
        while len(queue) > 0:
            if current_queue_size == 0:
                current_queue_size = len(queue)
                # in every minute, each rotten turns the fresh to rotten.
                minutes += 1
            current_orange = queue.popleft()
            current_queue_size -= 1
            row = current_orange[0]
            col = current_orange[1]
            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
                    continue
                if grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    fresh_oranges -= 1
                    queue.append([next_row, next_col])
        if fresh_oranges != 0:
            return -1
        return minutes



