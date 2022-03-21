import sys; input=sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

answer = -1
for i in range(n-2):
    for j in range(n-2):
        _sum = sum([board[a][b] for a in range(i, i+3) for b in range(j, j+3)])
        answer = max(answer, _sum)
print(answer)