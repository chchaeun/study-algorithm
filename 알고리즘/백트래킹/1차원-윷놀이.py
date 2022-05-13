
n, m, k = map(int, input().split())
turn = list(map(int, input().split()))

location = [1 for _ in range(k+1)]

global answer
answer = 0

def choose(count):
    global answer
    if count == n:
        temp = 0
        for loc in location[1:]:
            if loc>=m: temp += 1
            answer = max(answer, temp)
        return
    for i in range(1, k+1):
        location[i] += turn[count]
        choose(count + 1)
        location[i] -= turn[count]

choose(0)

print(answer)