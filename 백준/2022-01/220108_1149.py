import sys

input = sys.stdin.readline

n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]

# 0: R, 1: G, 2: B

# 반복

for i in range(1, n):
    for j in range(0, 3):
        b[i][j] = min(b[i-1][(j+1)%3], b[i-1][(j+2)%3]) + b[i][j]
print(min(b[n-1][0], b[n-1][1], b[n-1][2]))


# 재귀 (시간초과)

# _min = 1000001
# def f(number, rgb, sum):
#     global _min
#     if number == n-1:
#         _min = min(sum, _min)
#         return
#     for i in [1, 2]:
#         f(number+1, (rgb+i)%3, sum+b[number+1][(rgb+i)%3])

# for i in range(0, 3):
#     f(0, i, b[0][i])

# print(_min)
