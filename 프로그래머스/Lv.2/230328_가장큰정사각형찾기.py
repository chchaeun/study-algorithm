def solution(board):
    w = len(board[0])
    h = len(board)
    m = max(w, h)

    for k in range(m, 0, -1):
        for i in range(h):
            for j in range(w):
                if i+k > h or j+k > w:
                    continue
                if isSquare(board, k, i, j):
                    return k * k
    return 0

def isSquare(board, width, y, x):
    for i in range(y, y+width):
        for j in range(x, x+width):
            if board[i][j] == 0:
                return False
    return True


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))