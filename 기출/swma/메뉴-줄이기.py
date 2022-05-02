from itertools import combinations
n, m, k = map(int, input().split())
consumer = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for m in combinations(range(m), m-k):
    remain = set()
    for i in range(n):
        for j in m:
            if consumer[i][j] >= 5:
                remain.add(i)
                break
    answer = max(len(remain), answer)
print(answer)