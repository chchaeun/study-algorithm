from collections import deque

N = int(input())
init = [list(map(int, input().split())) for _ in range(N)]

def move(board):
    nboard = [[0 for _ in range(N)] for _ in range(N)]
    merge = False

    for i in range(N):
        stack = deque()
        for j in range(N):
            num = board[i][j]
            if num == 0:
                continue
            if stack and stack[-1] == num and not merge:
                stack[-1] = num * 2
                merge = True
                continue
            stack.append(num)
            merge = False
        print(stack) 
        for j in range(N-len(stack), N):
            nboard[i][j] = stack.popleft()

    return nboard

def rotate(board, direction):
    nboard = [[0 for _ in range(N)] for _ in range(N)]

    if direction == 1:
        for r in range(N):
            for c in range(N):
                nboard[c][N-1-r] = board[r][c]
    if direction == 2:
        for r in range(N):
            for c in range(N):
                nboard[N-1-c][N-1-r] = board[c][r]
    if direction == 3:
        for r in range(N):
            for c in range(N):
                nboard[N-1-c][r] = board[r][c]

    return nboard

def nPr(board, depth):
    if depth == 6:
        find_max(board)
        return

    nPr(move(board), depth + 1)
    nPr(rotate(move(rotate(board, 1)), 3), depth + 1)
    nPr(rotate(move(rotate(board, 2)), 2), depth + 1)
    nPr(rotate(move(rotate(board, 3)), 1), depth + 1)

global answer
answer = 0

def find_max(board):
    global answer
    for b in board:
        answer = max(answer, max(b))

def deepcopy(board):
    return [b[:] for b in board]
    
# nPr(init, 0)
print(answer)

# print(move(init))
# print(rotate(move(rotate(init, 1)), 3))
print(rotate(move(rotate(init, 2)), 2))
# print(rotate(move(rotate(init, 3)), 1))
