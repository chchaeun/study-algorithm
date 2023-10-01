dice = list(map(int, input().split()))

board = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

global answer
answer = 0

def backtracking(location, total, depth):
    global answer
    if depth == 10:
        answer = max(answer, total)
        return
    
    for i in range(4):
        x = location[i]

        if len(board[x]) == 2:
            x = board[x][1]
        else:
            x = board[x][0]
        
        for _ in range(1, dice[depth]):
            x = board[x][0]
            
        if x == 32 or (x < 32 and x not in location):
            prev = location[i]
            location[i] = x

            backtracking(location, total + score[x], depth + 1)

            location[i] = prev

backtracking([0, 0, 0, 0], 0, 0)
print(answer)