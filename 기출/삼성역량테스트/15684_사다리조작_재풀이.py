N, M, H = map(int, input().split())
board = [[False for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True

empty_arr = []
def empty():
    for i in range(H):
        for j in range(N-1):
            if not board[i][j] and not board[i][j+1]:
                empty_arr.append((i, j))

def possible(nboard, arr):
    for a in arr:
        y, x = a

        if (x-1 >= 0 and nboard[y][x-1]) or nboard[y][x] or nboard[y][x+1]:
            return False
        else:
            nboard[y][x] = True

    return True

def backtracking(arr, depth):
    if len(arr) == 3 or len(empty_arr) == depth:
        nboard = [b[:] for b in board]
        if possible(nboard, arr):
            search(len(arr), nboard)
        return

    arr.append(empty_arr[depth])
    backtracking(arr, depth + 1)

    arr.pop()
    backtracking(arr, depth + 1)


def search(numofadd, nboard):
    global answer
    if numofadd > answer:
        return

    result = True

    for i in range(N):
        x = i
        for j in range(H):
            if nboard[j][x]:
                x += 1
            elif x - 1 >= 0 and nboard[j][x-1]:
                x -= 1
        if x != i:
            result = False
            break

    if result:
        answer = numofadd

global answer
answer = int(1e9)
empty()
backtracking([], 0)

print(answer if answer < 4 else -1)