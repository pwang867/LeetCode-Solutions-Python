"""
size of the board: m, n
bomb = -1

number of bombs: b

"""

import random


class MineSweeper:
    def __init__(self, m, n, b):
        # check m, n
        if m <= 0 or n <= 0:
            raise ValueError("size of board can not be empty")
        if b <= 0 or b > m * n:
            raise ValueError("number of bombs are out of bound")
        self.m = m
        self.n = n
        self.b = b

        self.board = [[0] * n for _ in range(m)]
        # "#": undiscovered, 'b': bomb, "0-8"
        self.ui = [["#"] * n for _ in range(m)]
        self.fill_bombs()
        self.display()

    def fill_bombs(self):
        idx = [(i, j) for i in range(self.m) for j in range(self.n)]
        random.shuffle(idx)
        selected = idx[:self.b]
        for i, j in selected:
            self.board[i][j] = -1  # mark the cell (i,j) as a bomb

    def left_click(self, i, j):
        if self.ui[i][j] != "#":
            return
        if self.board[i][j] == -1:
            print("game over")
            return
        self.dfs(i, j)
        self.display()

    def dfs(self, i, j):
        if self.ui[i][j] != "#":
            return
        cnt = self.count_bombs(i, j)
        self.ui[i][j] = str(cnt)
        if cnt > 0:
            return
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
            x, y = i + di, j + dj
            if 0 <= x < self.m and 0 <= y < self.n and self.ui[x][y] == "#":
                self.dfs(x, y)

    def count_bombs(self, i, j):
        cnt = 0
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] == -1:
                    cnt += 1
        return cnt

    def display(self):
        # print(self.ui)
        print("\n")
        for row in self.ui:
            print(row)


if __name__ == "__main__":
    random.seed(14)
    game = MineSweeper(5, 5, 5)
    print(game.board)
    # game.display()
    game.left_click(0, 0)
    game.left_click(1, 2)


