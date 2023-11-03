import sys
input = sys.stdin.readline

N = int(input().rstrip())
sticks = []
for _ in range(N):
    height = int(input().rstrip())
    sticks.append(height)

count = 1
_max = sticks[-1]
for stick in reversed(sticks):
    if stick > _max:
        count += 1
        _max = stick

print(count)