def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:    
        square = check_square(m, n, board)
        if not square: break
        board = clear(square, board)
    for i in board:
        for j in i:
            if not j:
                answer+=1
    return answer

def check_square(m, n, board):
    square = []
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    for i in range(m-1):
        for j in range(n-1):
            if not board[i][j]: continue
            count=0
            for k in range(3):
                nx = i+dx[k]
                ny = j+dy[k]
                if board[i][j]==board[nx][ny]:
                    count+=1
                else: break
            if count==3:
                square.append((i, j))
    return square

def clear(square, board):
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    visited = []
    for s in square:
        for k in range(4):
            nx = s[0]+dx[k]
            ny = s[1]+dy[k]
            if board[nx][ny] and (nx, ny) not in visited:
                visited.append((nx, ny))
                if nx==0:
                    board[nx][ny]=""
                else:
                    for i in range(nx, 0, -1):
                        board[i][ny]=board[i-1][ny]
                        board[i-1][ny]=""
    return board


testm = [6]
testn = [5]
testb = [
    ["CCZXZ",
"CCZXZ",
"XXZXZ",
"AAZAA",
"AAAAA",
"ZAAXX"]
]
for tm, tn, b in zip(testm, testn, testb):
    print(solution(tm, tn, b))
    