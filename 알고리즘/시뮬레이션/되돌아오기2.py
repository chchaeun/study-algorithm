import sys; input=sys.stdin.readline
order = input().strip()

x, y = 0, 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cur = 0
mapper = {'L':-1, 'R':1}
for i in range(len(order)):
    if order[i]=='F':
        x += dx[cur]
        y += dy[cur]
    else:
        cur = (cur+4+mapper[order[i]])%4
    if (x, y) == (0, 0):
        print(i+1)
        break
else: print(-1)