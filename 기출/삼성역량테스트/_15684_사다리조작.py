n, m, h = map(int, input().split())
answer = int(1e9)
ladder = [[False for _ in range(n-1)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = True

def check():
    for x in range(n-1):
        current = x
        for y in range(h):
            if current < n-1 and ladder[y][current]:
                current += 1
                continue
            if current-1 >= 0 and ladder[y][current-1]:
                current -= 1
                continue
        if current != x:
            return False
    return True

MAX = 3   
def new_ladder(depth, y, x):
    global answer

    if depth > MAX:
        return
    
    if check():
        answer = min(depth, answer)

    for i in range(y, h):
        for j in range(n-1):
            if ladder[i][j] or 0 <= j-1 and ladder[i][j-1] or j+1 < n-1 and ladder[i][j+1]:
                continue

            ladder[i][j] = True
            new_ladder(depth + 1, i, j)
            ladder[i][j] = False

new_ladder(0, 0, 0) 

answer = -1 if answer == int(1e9) else answer

print(answer)
