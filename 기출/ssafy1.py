import heapq
from collections import deque

INF = int(1e9)

T = int(input())

for case in range(1, T+1):
    N, K = map(int, input().split())
    levels = list(map(int, input().split()))
    heapq.heapify(levels)

    answer = 0

    min_level = INF
    team = deque()

    for _ in range(N):
        level = heapq.heappop(levels)
        while level - min_level > K:
            team.popleft()
            if team:
                min_level = team[0]
            else:
                min_level = INF

        team.append(level)
        min_level = team[0]
        answer = max(answer, len(team))

    print("#{} {}".format(case, answer))