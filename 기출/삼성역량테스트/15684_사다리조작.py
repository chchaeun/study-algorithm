global n, m, h, answer
n, m, h = map(int, input().split())
answer = int(1e9)
EMPTY = -1
ladder = [[-1 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = b
    ladder[a-1][b] = b-1

def try_ladder(ladder):
    global n, h
    for i in range(n):
        visited = [[False for _ in range(n)] for _ in range(h)]
        visited[0][i] = True
        x = i
        for j in range(h):
            if ladder[j][x] == EMPTY:
                continue
            nx = ladder[j][x]
            if not visited[j][nx]:
                x = nx
                visited[j][x] = True
        
        if i != x:
            return False
    return True


empty_ladder = []
for i in range(h):
    for j in range(n-1):
        if ladder[i][j] == EMPTY and ladder[i][j+1] == EMPTY:
            if j+2 >= n or ladder[i][j+2] == EMPTY:
                empty_ladder.append((i, j))

def try_new_ladder(case):
    global n, h
    for c in case:
        y, x = c
        ladder[y][x+1] = x
        ladder[y][x] = x+1

    return try_ladder(ladder)

def comb(case, num, depth):
    global answer
    if len(case) == num:
        if try_new_ladder(case):
            answer = min(answer, num)
        return 
    if depth == len(empty_ladder):
        return

    a, b = empty_ladder[depth]
    for c in case:
        i, j = c
        if a==i and abs(b-j) < 3:
            continue
    else:
        case.append(empty_ladder[depth])
        comb(case, num, depth + 1)

        case.pop()
        comb(case, num, depth + 1)

for i in range(1, 4):
    comb([], i, 0)

if answer == int(1e9):
    print(-1)
else:
    print(answer)

# 사다리 놓는 방식 바꾸기!!