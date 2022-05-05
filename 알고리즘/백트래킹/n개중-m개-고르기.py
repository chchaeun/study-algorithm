n, m = map(int, input().split())
answer = [-1]
def choose(count):
    if m==count:
        print(*answer[1:])
        return
    for i in range(1, n+1):
        if answer[-1]<i:
            answer.append(i)
            choose(count+1)
            answer.pop()
        
choose(0)