import sys
sys.setrecursionlimit(10**6)
def solution(grid):
    # 화살표 위 오른쪽 아래 왼쪽 0 1 2 3
    answer = []
    
    global board
    board = [[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(4)]
    
    global count
    count = 0
    
    for k in range(4):
        for i in range(len(board[k])):
            for j in range(len(board[k][i])):
                if board[k][i][j] == 0:
                    count = 0
                    shoot(grid, k, i, j)
                    if count != 0: answer.append(count)
    return sorted(answer)                
    
def shoot(grid, arrow, row, col):
    if board[arrow][row][col] == 1:
        return
    board[arrow][row][col] = 1
    
    global count
    count+=1
    
    arrows = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    turn = {'S':0, 'L':-1, 'R':1}
    
    nrow = (row+arrows[arrow][0])%len(grid)
    ncol = (col+arrows[arrow][1])%len(grid[0])
    narrow = (arrow + turn[grid[nrow][ncol]])%4
    
    shoot(grid, narrow, nrow, ncol)
    
    
# grid	result
# ["SL","LR"]	[16]
# ["S"]	[1,1,1,1]
# ["R","R"]	[4,4]

solution(["R","R"])
print(board)