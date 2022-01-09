import sys
input = sys.stdin.readline
s1 = [""]+list(input().strip())
s2 = [""]+list(input().strip())

board = [[0 for _ in range(len(s2))] for _ in range(len(s1))]


for i in range(1, len(board)):
    for j in range(1, len(board[i])):
        if s1[i] == s2[j]:
            board[i][j] = board[i-1][j-1]+1
        else:
            board[i][j] = max(board[i][j-1], board[i-1][j])

print(board[len(s1)-1][len(s2)-1])
    