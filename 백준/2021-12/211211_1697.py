from collections import deque
n, k = map(int, input().split())

dq = deque([n])
max = 100001
dist = [0 for _ in range(max)]
while dq:
    v = dq.popleft()
    if v==k:
        break
    for nv in (v+1, v-1, v*2):
        # 조건문 순서 바뀌면 인덱스 에러
        if 0<=nv<max and not dist[nv]:
            dist[nv] = dist[v]+1
            dq.append(nv)
    
print(dist[k])

# 트리 깊이 찾는 문제 -> 최단경로처럼 풀기
