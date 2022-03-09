# https://www.lintcode.com/problem/1022/description
from typing import List
class Solution:
    def valid_tic_tac_toe(self, board: List[str]) -> bool:
        state = []
        x_size = 0
        o_size = 0
        total_letters = 0
        for string in board:
            for letter in string:
                if letter == "X":
                    x_size += 1
                    total_letters += 1
                elif letter == "O":
                    o_size += 1
                    total_letters += 1
                state.append(letter)
        winning_lines = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6], [1, 4, 7],[2, 5, 8],[0, 4, 8], [2, 4, 6]];
        count = 0
        for line in winning_lines:
            if state[line[0]] == state[line[1]] == state[line[2]]:
                count += 1
        if count == 1 and x_size - o_size == 1:
            return True
        if count == 1:
            return False
        if count > 1:
            return False
        if total_letters == 1:
            for letter in state:
                if letter == "O":
                    return False
        if not (x_size == o_size or x_size == o_size + 1):
            return False
        return True