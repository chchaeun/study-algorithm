N = int(input())

t = [0 for _ in range(N)]
p = [0 for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    t[i], p[i] = a, b


global answer
answer = 0

def backtracking(now, _sum):
    if now + t[now] > N:
        return

    global answer
    answer = max(answer, _sum)

    for j in range(now+t[now], N):
        backtracking(j, _sum + p[j])
        
for i in range(N):
    backtracking(i, p[i])
print(answer)