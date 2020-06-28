import random


class MineSweep:
    def __init__(self, row, col, nbombs):
        if row <= 0 or col <= 0 or nbombs <= 0:
            raise ValueError("Empty board or bombs are not allowed")
        self.row = row
        self.col = col
        self.flags = 0
        self.under_flags = {}  # {(i, j): prev char under flag}
        self.nbombs = nbombs
        self.n_uncovered = 0
        self.bombs = self.generate_bombs()  # {(i, j)} for bombs
        self.board = [["#"]*self.col for _ in range(self.row)]
        self.dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.display()

    def generate_bombs(self):
        ids = [(i, j) for i in range(self.row) for j in range(self.col)]
        bombs = random.sample(ids, self.nbombs)
        print("bombs generated: ", bombs)
        return set(bombs)

    def display(self):
        print("Current Board:")
        for row in self.board:
            print(row)
        print("Bombs: {}/{}".format(self.flags, self.nbombs))
        if self.check_win():
            print("You win!")

    def check_win(self):
        if self.n_uncovered + self.nbombs == self.row * self.col:
            return True
        # if set(self.under_flags.keys()) == self.bombs:
        #     return True

    def left_click(self, i, j):
        print("\n")
        print("left click on: ", i, j)
        if 0 <= i < self.row and 0 <= j < self.col and self.board[i][j] == "#":
            if (i, j) in self.bombs:
                self.board[i][j] = "X"
                print("Game Over")
            else:
                self.uncover(i, j)
        self.display()

    def uncover(self, i, j):
        # self.board[i][j] must be "#" when self.uncover() is called
        self.n_uncovered += 1
        cnt = self.count_bombs_nearby(i, j)
        self.board[i][j] = str(cnt)
        if cnt > 0:   # only recurse when cnt == 0
            return
        for di, dj in self.dirs:
            r, c = i + di, j + dj
            if 0 <= r < self.row and 0 <= c < self.col and self.board[r][c] == "#":
                self.uncover(r, c)

    def count_bombs_nearby(self, i, j):
        cnt = 0
        for di, dj in self.dirs:
            r, c = i + di, j + dj
            if (r, c) in self.bombs:
                cnt += 1
        return cnt

    def right_click(self, i, j):
        print("\n")
        print("Right Click on: ", i, j)
        if self.flags >= self.nbombs:
            print("Too many flags")
        if self.board[i][j] != "B":
            self.under_flags[(i, j)] = self.board[i][j]
            self.board[i][j] = "B"
            self.flags += 1
        else:
            prev = self.under_flags[(i, j)]
            self.board[i][j] = prev
            self.flags -= 1
            del self.under_flags[(i, j)]
        self.display()



if __name__ == "__main__":
    random.seed(15)
    game = MineSweep(5, 5, 3)
    game.left_click(0, 1)
    game.left_click(1, 4)
    game.right_click(0, 1)
    game.right_click(0, 1)
    game.right_click(0, 0)
    game.right_click(3, 3)
    game.left_click(3, 4)
    game.left_click(4, 3)
    game.right_click(4, 4)


