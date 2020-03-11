# method 2, make it extensible/generalized

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        N = 3
        NUM_PLAYER = 2
        marks = "XO"
        players = "AB"
        remain = N * N
        board = [[""] * N for _ in range(N)]
        rows = [[0] * N for _ in range(NUM_PLAYER)]
        cols = [[0] * N for _ in range(NUM_PLAYER)]
        diag = [0] * NUM_PLAYER
        adiag = [0] * NUM_PLAYER

        for i, move in enumerate(moves):
            x, y = move
            if x < 0 or x >= N or y < 0 or y >= N or board[x][y] != "":
                continue
            remain -= 1
            iplayer = i % 2
            board[x][y] = marks[iplayer]
            # row
            rows[iplayer][x] += 1
            if rows[iplayer][x] == N:
                return players[iplayer]
            # col
            cols[iplayer][y] += 1
            if cols[iplayer][y] == N:
                return players[iplayer]
            # diagonal
            if x == y:
                diag[iplayer] += 1
                if diag[iplayer] == N:
                    return players[iplayer]
            # anti-diagonal
            if x + y == N - 1:
                adiag[iplayer] += 1
                if adiag[iplayer] == N:
                    return players[iplayer]
            if remain == 0:
                return "Draw"
        return "Pending"


# method 1, simply check the neighbors in the board
class Solution1(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [[""] * 3 for _ in range(3)]
        letters = ["A", "B"]
        for i, move in enumerate(moves):
            p, q = move
            grid[p][q] = letters[i % 2]
            if self.check(grid, p, q):
                return letters[i % 2]
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"

    def check(self, grid, p, q):
        if grid[p][0] == grid[p][1] == grid[p][2]:
            return True
        if grid[0][q] == grid[1][q] == grid[2][q]:
            return True
        if p == q:
            if grid[0][0] == grid[1][1] == grid[2][2]:
                return True
        if p + q == 2:
            if grid[2][0] == grid[1][1] == grid[0][2]:
                return True
        return False


"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""

