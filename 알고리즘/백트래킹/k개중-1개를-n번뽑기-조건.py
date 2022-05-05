k, n = map(int, input().split())

answer = [-1, -1]
def choose(count):
    if n==count:
        print(*answer[2:])
        return
    for i in range(1, k+1):
        if answer[-1]!=i or answer[-2]!=i:
            answer.append(i)
            choose(count+1)
            answer.pop()
choose(0)