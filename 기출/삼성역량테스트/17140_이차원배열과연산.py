from collections import Counter
import heapq
from copy import deepcopy

answer = 0
r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

rlen, clen = 3, 3
is_row = True

while True:
    if r<=len(board) and c<=len(board[0]) and board[r-1][c-1] == k:
        print(answer)
        break
    if answer == 101:
        print(-1)
        break

    nboard = []
    rlen, clen = len(board), len(board[0])
    if rlen < clen:
        board = list(zip(*board))
        is_row = False
    clen = 0
    for b in board:
        counts = list(map(lambda x: (x[1], x[0]), list(Counter(b).items())))
        heapq.heapify(counts)
        temp = []
        rlen = len(counts)

        for _ in range(rlen):
            t = list(heapq.heappop(counts))
            if t[1] == 0:
                continue
            temp.extend(reversed(t))

        clen = max(clen, len(temp))
        nboard.append(temp)

    for nb in nboard:
        if len(nb) < clen:
            nb.extend([0]*(clen - len(nb)))

    board = deepcopy(nboard)

    if not is_row:
        board = list(zip(*board))
        is_row = True

    answer += 1
    