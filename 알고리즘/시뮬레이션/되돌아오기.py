import sys; input=sys.stdin.readline
n = int(input().strip())
mapper = {
    'N':0,
    'E':1,
    'S':2, 
    'W':3
}
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cur = 0
answer = 0
x, y = 0, 0
for _ in range(n):
    direct, move = input().split()
    cur = mapper[direct]
    for m in range(int(move)):
        x += dx[cur]
        y += dy[cur]
        answer+=1
        if (x, y) == (0, 0):
            print(answer)
            exit()
print(-1)