EMPTY = -1
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C, M = map(int, input().split())
board = [[EMPTY for _ in range(C)] for _ in range(R)]
sharks = [None for _ in range(M)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r-1, c-1, d-1

    board[r][c] = i
    sharks[i] = [r, c, s, d, z]

def total_move():
    nboard = [[EMPTY for _ in range(C)] for _ in range(R)]

    for snum, shark in enumerate(sharks):
        if shark == None:
            continue

        r, c = shark_move(snum, shark)
        if nboard[r][c] == EMPTY:
            nboard[r][c] = snum
        else:
            old_size = sharks[nboard[r][c]][4]
            new_size = sharks[snum][4]

            if old_size > new_size:
                sharks[snum] = None
            if old_size < new_size:
                sharks[nboard[r][c]] = None
                nboard[r][c] = snum
    
    return nboard

def shark_move(snum, shark):
    r, c, s, d, z = shark
    dr, dc = direction[d]
    for _ in range(s):
        nr, nc = r + dr, c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            if d % 2 == 0:
                d += 1
            else:
                d -= 1

            dr, dc = direction[d]
            nr, nc = r + dr, c + dc
        
        if 0 <= nr < R and 0 <= nc < C:
            r, c = nr, nc

    sharks[snum] = [r, c, s, d, z]
    return r, c

answer = 0
for king in range(C):
    for row in range(R):
        snum = board[row][king]
        if snum != EMPTY:
            answer += sharks[snum][4]
            sharks[snum] = None
            board[row][king] = EMPTY
            break
    
    board = total_move()

print(answer)
