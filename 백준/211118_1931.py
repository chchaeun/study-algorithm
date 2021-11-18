import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0], x[1]))
# 키 두 개로 정렬 안했을 때 반례
# (5, 5) 다음에 (5, 7) 나오면 (5, 5)랑 (5, 7) 둘 다 들어갈 수 있는데 
# (5, 7) 다음에 (5, 5) 나오면 (5, 7)을 빼버림
 
dq = deque()
top=-1
for i in range(len(arr)):
    if len(dq) == 0:
        dq.append(arr[i])
        top+=1
        continue
    if dq[top][1] > arr[i][0]:
        if dq[top][1] > arr[i][1]:
            # Greedy: 얼마나 적게 시간 소모하느냐보다 얼마나 빨리 끝나느냐가 관건
            dq.pop()
            dq.append(arr[i])
    else:
        dq.append(arr[i])
        top+=1
        
print(len(dq))