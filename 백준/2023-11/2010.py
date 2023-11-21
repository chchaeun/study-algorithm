import sys

input = sys.stdin.readline

N = int(input())

answer = 0

for _ in range(N):
    plug = int(input())
    answer += plug - 1

answer += 1

print(answer)