N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(b) for b in board])

def find_line(x, y, d1, d2):
    line = [[False for _ in range(N)] for _ in range(N)]
    line[x][y] = True

    ly, ry = y, y

    while True:
        x += 1
        if d1 > 0:
            ly -= 1
        else:
            ly += 1

        if d2 > 0:
            ry += 1
        else:
            ry -= 1

        for i in range(ly, ry + 1):
            line[x][i] = True

        d1, d2 = d1-1, d2-1

        if ly >= ry:
            break

    return line

def calculate(x, y, d1, d2):
    population = [0 for _ in range(5)]
    line = find_line(x, y, d1, d2)
    for i in range(N):
        for j in range(N):
            if line[i][j]:
                continue
            if 0 <= i < x+d1 and 0 <= j <= y:
                line[i][j] = 0
                index = 0
            if 0 <= i <= x+d2 and y < j <= N-1:
                line[i][j] = 1
                index = 1
            if x+d1 <= i <= N-1 and 0 <= j < y-d1+d2:
                line[i][j] = 2
                index = 2
            if x+d2 < i <= N-1 and y-d1+d2 <= j <= N-1:
                line[i][j] = 3
                index = 3

            population[index] += board[i][j]

    population[4] = total - sum(population[:4])

    return max(population) - min(population)


answer = int(1e9)
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if d1 > y or d2 > N-1-y or d1+d2 > N-1-x:
                    continue

                answer = min(calculate(x, y, d1, d2), answer)

print(answer)