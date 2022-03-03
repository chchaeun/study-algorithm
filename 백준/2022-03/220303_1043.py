from copy import deepcopy
import sys; input=sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth = set(truth[1:]) if truth[0]!=0 else 0
party = [[0 for _ in range(51)] for _ in range(m)]
for i in range(m):
    for j in list(map(int, input().split()))[1:]:
        party[i][j] = 1 # 파티에 참석

if not truth:
    print(m)
    exit()

def checkParty(pnum):
    for i in truth:
        if party[pnum][i]==1:
            return False
    return True

def getTruth():
    newTruth = deepcopy(truth)
    for i in range(m):
        if not checkParty(i):
            for j in range(51):
                if party[i][j]==1:
                    newTruth.add(j)
    return newTruth

answer = 0
while True:
    newTruth = getTruth()
    if truth==newTruth:
        for i in range(m):
            if checkParty(i):
                answer += 1
        break
    else:
        truth = newTruth
print(answer)