# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        state = [
            [None, None, None],
            [None, None, None],
            [None, None, None]]

        for i, move in enumerate(moves):
            row, col = move[0], move[1]
            if i % 2 == 0:
                state[row][col] = "X"
            else:
                state[row][col] = "O"

        if state[0][0] == state[0][1] == state[0][2] == "O":
            return "B"
        elif state[0][0] == state[0][1] == state[0][2] == "X":
            return "A"

        if state[1][0] == state[1][1] == state[1][2] == "O":
            return "B"
        elif state[1][0] == state[1][1] == state[1][2] == "X":
            return "A"
        if state[2][0] == state[2][1] == state[2][2] == "O":
            return "B"
        elif state[2][0] == state[2][1] == state[2][2] == "X":
            return "A"
        if state[0][0] == state[1][0] == state[2][0] == "O":
            return "B"
        elif state[0][0] == state[1][0] == state[2][0] == "X":
            return "A"
        if state[0][1] == state[1][1] == state[2][1] == "O":
            return "B"
        elif state[0][1] == state[1][1] == state[2][1] == "X":
            return "A"

        if state[0][2] == state[1][2] == state[2][2] == "O":
            return "B"
        elif state[0][2] == state[1][2] == state[2][2] == "X":
            return "A"
        if state[0][0] == state[1][1] == state[2][2] == "O":
            return "B"
        elif state[0][0] == state[1][1] == state[2][2] == "X":
            return "A"

        if state[2][0] == state[1][1] == state[0][2] == "O":
            return "B"
        elif state[2][0] == state[1][1] == state[0][2] == "X":
            return "A"
        for i in range(3):
            for j in range(3):
                if state[i][j] == None:
                    return "Pending"
        return "Draw"

class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        num_X, num_O = 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 'X':
                    num_X += 1
                if board[i][j] == 'O':
                    num_O += 1
        if not (num_X == num_O or num_X == num_O + 1):
            return False

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    return num_X == num_O + 1
                if board[i][0] == 'O':
                    return num_X == num_O

        # check cols if there is a winner
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == 'X':
                    return num_X == num_O + 1
                if board[0][j] == 'O':
                    return num_X == num_O
        # check one diagnal if there is a winner
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return num_X == num_O + 1
            if board[0][0] == 'O':
                return num_X == num_O
        # check another diagnal if there is a winner
        if board[0][2] == board[1][1] == board[2][0]:
            if board[2][0] == 'X':
                return num_X == num_O + 1
            if board[2][0] == 'O':
                return num_X == num_O
        return True