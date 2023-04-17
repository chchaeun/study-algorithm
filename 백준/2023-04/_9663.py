n = int(input())

answer = 0
board = [0 for _ in range(n)]
visited = [False for _ in range(n)]

def promising(y):
    for i in range(y):
        if board[y] == board[i] or y-i == abs(board[y]-board[i]):
            return False

    return True

def queen(y):
    global answer
    if y == n:
        answer += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        board[y] = i
        if promising(y):
            visited[i] = True
            queen(y+1)
            visited[i] = False

queen(0)
print(answer)