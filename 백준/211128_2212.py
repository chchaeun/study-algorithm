import sys
import heapq
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

n_arr = list(map(int, sys.stdin.readline().split()))

n_arr.sort()
hq = []
for i in range(n-1):
    heapq.heappush(hq, n_arr[i+1]-n_arr[i])
result=0
for i in range(n-k):
    result+=heapq.heappop(hq)
    
print(result)    
