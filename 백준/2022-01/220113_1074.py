import sys

num, row, col = map(int, sys.stdin.readline().split())

# board: 사분면
board=[]

state =[(False, False), (False, True), (True, False), (True, True)]
def f(n, r, c):
    if n==0:
        return
    half = 2**(n-1)
    r_state = r>=half
    c_state = c>=half
    if not r_state and not c_state:
        board.append(0)
    elif not r_state and c_state:
        board.append(1)
        c -= half
    elif r_state and not c_state:
        board.append(2)
        r -= half
    else:
        board.append(3)
        r -= half
        c -= half
    f(n-1, r, c)

f(num, row, col)

answer = 0
for i in range(num):
    answer += board[i]*(4**(num-1-i))
    
print(answer)
print(board)