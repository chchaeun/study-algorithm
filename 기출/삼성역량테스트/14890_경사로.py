n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for _ in range(2):
    for b in board:
        ramp = [False for _ in range(n)]
        i = 0
        road = True
        
        while i < n-1:
            if b[i] == b[i+1] - 1:
                if i - l + 1 < 0:
                    road = False
                    break

                for j in range(l):
                    if ramp[i-j] or b[i-j] != b[i]:
                        road = False
                        break
                    ramp[i-j] = True

            if b[i] == b[i+1] + 1:
                if i + l >= n:
                    road = False
                    break

                for j in range(1, l+1):
                    if ramp[i+j] or b[i+j] != b[i]-1:
                        road = False
                        break
                    ramp[i+j] = True

            if abs(b[i] - b[i+1]) > 1:
                road = False
            i += 1

        if road:
            answer += 1
    board = list(zip(*board))
print(answer)