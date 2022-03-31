n = int(input())
glass = [list(input().strip()) for _ in range(n)]
k = int(input())

direct = (k-1)//n
remain = (k-1)%n
if direct == 0:
    x, y = 0, remain
elif direct == 1:
    x, y = remain, n-1
elif direct == 2:
    x, y = n-1, n-1-remain
elif direct == 3:
    x, y = n-1-remain, 0

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

count = 0
while True:
    if glass[x][y]=='/':
        direct = 3-direct
    else:
        direct = direct^1
    x += dx[direct]
    y += dy[direct]
    count += 1
    if not (0<=x<n and 0<=y<n):
        break
print(count)