def get_interest_of_competition(matrix):
    score = 0
    while True:
        score += get_sum(matrix)
        if not has_elimination(matrix):
            return score


def get_sum(matrix):
    if not matrix or not matrix[0]:
        return 0
    return sum(map(sum, matrix))


def has_elimination(matrix):
    if not matrix or not matrix[0]:
        return False
    R, C = len(matrix), len(matrix[0])
    levels = [[0] * C for _ in range(R)]
    cnts = [[0] * C for _ in range(R)]

    for i in range(R):
        # left
        val = 0
        for j in range(C):
            levels[i][j] += val
            if val != 0:
                cnts[i][j] += 1
            if matrix[i][j] != 0:
                val = matrix[i][j]
        # right
        val = 0
        for j in range(C - 1, -1, -1):
            levels[i][j] += val
            if val != 0:
                cnts[i][j] += 1
            if matrix[i][j] != 0:
                val = matrix[i][j]
    for j in range(C):
        # top
        val = 0
        for i in range(R):
            levels[i][j] += val
            if val != 0:
                cnts[i][j] += 1
            if matrix[i][j] != 0:
                val = matrix[i][j]
        # bottom
        val = 0
        for i in range(R - 1, -1, -1):
            levels[i][j] += val
            if val != 0:
                cnts[i][j] += 1
            if matrix[i][j] != 0:
                val = matrix[i][j]

    # get average
    elim = False
    for i in range(R):
        for j in range(C):
            if matrix[i][j] > 0 and cnts[i][j] > 0:
                if levels[i][j] * 1.0 / cnts[i][j] > matrix[i][j]:
                    elim = True
                    matrix[i][j] = 0
    return elim

matrix = [[1,1,1],[1,2,1],[1,1,1]]
print(get_interest_of_competition(matrix))
