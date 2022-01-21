import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]
