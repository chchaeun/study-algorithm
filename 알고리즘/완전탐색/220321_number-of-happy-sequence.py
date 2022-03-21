import sys; input=sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def is_happiness(seq):
    count = 1
    _max = 1
    for i in range(1, len(seq)):
        if seq[i-1]==seq[i]:
            count += 1
        else: 
            count = 1
        _max = max(count, _max)
    if _max>=m: return True
    else: return False

answer = 0
rboard = list(map(list, zip(*board)))
for b in [board, rboard]:
    for i in range(n):
        if is_happiness(b[i]):
            answer+=1
print(answer)