import sys; input=sys.stdin.readline
import heapq
t = int(input().strip())
for _ in range(t):
    heap = []
    k = int(input().strip())
    for _ in range(k):
        op, n = input().split()
        n=int(n)
        if op=='I':
            heapq.heappush(heap, n)
        elif heap and n==-1:
            heapq.heappop(heap)
        elif heap and n==1:
            heap.remove(max(heap))
            heapq.heapify(heap)
    if not heap:
        print("EMPTY")
    else:
        print(max(heap), min(heap))
        
# 최대힙최소힙따로 구현하고 상태 맞춰주는 배열 따로 두기
