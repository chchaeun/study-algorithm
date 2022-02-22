from copy import deepcopy
import sys; input=sys.stdin.readline
n, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
unit = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def calculate(X, Y):
    return [[sum(i*j%1000 for i, j in zip(xrow, ycol)) for ycol in zip(*Y)] for xrow in X]

def divide(a, b):
    result = deepcopy(unit)
    while(b):
        if b%2:
            result = calculate(result, a)
        a = calculate(a, a)
        b//=2
    return result

board = divide(board, b)

for i in board:
    for j in i:
        print(j%1000, end=" ")
    print()