from collections import defaultdict

SUCCESS, FAIL = 1, 0

t = int(input())

for case in range(1, t+1):
    board = [list(map(int, input().split())) for _ in range(9)]

    answer = SUCCESS

    for i in range(9):
        checkHorizon = defaultdict(bool)  
        checkVertical = defaultdict(bool)  
        for j in range(9):
            if checkHorizon[board[i][j]]:
                answer = FAIL
            checkHorizon[board[i][j]] = True

            if checkVertical[board[j][i]]:
                answer = FAIL
            checkVertical[board[j][i]] = True

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            checkSquare = defaultdict(bool)
            for k in range(3):
                for l in range(3):
                    if checkSquare[board[i+k][j+l]]:
                        answer = FAIL
                    checkSquare[board[i+k][j+l]] = True

    print("#{} {}".format(case,answer))
