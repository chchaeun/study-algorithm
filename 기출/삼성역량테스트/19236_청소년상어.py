N = 4
EMPTY, SHARK = 0, -1
NUMOFFISH = 16
ANTICLOCKWISE = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

location = [[] for _ in range(NUMOFFISH+1)]
direction = [-1 for _ in range(NUMOFFISH+1)]
number = [[EMPTY for _ in range(N)] for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(0, len(temp), 2):
        num, dir = temp[j], temp[j+1] - 1
        location[num] = [i, j//2]
        direction[num] = dir
        number[i][j//2] = num

def fish_move(location, number, direction):
    for i in range(1, NUMOFFISH+1):
        if len(location[i]) == 0:
            continue

        y, x = location[i]
        
        for _ in range(8):
            dy, dx = ANTICLOCKWISE[direction[i]]
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and number[ny][nx] != SHARK:
                location[number[ny][nx]], location[number[y][x]] = [y, x], [ny, nx]
                if number[ny][nx] == EMPTY:
                    location[number[ny][nx]] = []
                number[ny][nx], number[y][x] = number[y][x], number[ny][nx]
                break
            direction[i] = (direction[i]+1)%8

    return location, number, direction

def shark_move(location, number, direction, y, x, d, score):
    location = [fl[:] for fl in location]
    number = [num[:] for num in number]
    direction = direction.copy()

    location, number, direction = fish_move(location, number, direction)

    dy, dx = ANTICLOCKWISE[d]
    for i in range(1, 4):
        ny, nx = y + dy * i, x + dx * i

        if not (0<=ny<N and 0<=nx<N) or number[ny][nx] == EMPTY:
            global answer
            answer = max(answer, score)
            continue

        before_num = number[ny][nx]
        location[before_num] = []
        number[ny][nx], number[y][x] = SHARK, EMPTY

        shark_move(location, number, direction, ny, nx, direction[before_num], score+before_num)

        location[before_num] = [ny, nx]
        number[ny][nx], number[y][x] = before_num, SHARK

global answer
answer = number[0][0]
location[number[0][0]] = []
number[0][0] = -1

shark_move(location, number, direction, 0, 0, direction[answer], answer)
print(answer)