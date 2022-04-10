n, m = map(int, input().split())
bomb = [int(input()) for _ in range(n)]

def getNewBomb():
    nbomb = []
    count = 1
    cur = -1
    for i in range(len(bomb)):
        if not nbomb or cur!=bomb[i]:
            nbomb.append(bomb[i])
            cur = bomb[i]
            count = 1
        elif cur == bomb[i]:
            nbomb.append(bomb[i])
            count += 1
        if (i==len(bomb)-1 or cur!=bomb[i+1]) and count >= m:
            for _ in range(count):
                nbomb.pop()
    return nbomb

while True:
    nbomb = getNewBomb()
    if bomb==nbomb: break
    else: bomb = nbomb

print(len(bomb))
for b in bomb:
    print(b)