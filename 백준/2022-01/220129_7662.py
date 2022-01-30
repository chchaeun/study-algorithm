'''
하나의 힙으로 구현하는 방법은 시간초과가 난다. 
최대힙/최소힙 두 개의 힙으로 구현하려면 삭제할 때 동기화가 필요하다.
state를 통해 현재 해당 id의 값이 이미 삭제된 값인지 확인한다.
삭제 작업이 끝나고 출력 전 마지막으로 값을 맞춰준다.
'''
import sys; input=sys.stdin.readline
import heapq
t = int(input().strip())
for _ in range(t):
    max_heap = []
    min_heap = []
    state = [False]*1000000
    k = int(input().strip())
    for id in range(k):
        op, n = input().split()
        n=int(n)
        if op=='I':
            heapq.heappush(max_heap, (-n, id))
            heapq.heappush(min_heap, (n, id))
            state[id]=True
        elif min_heap and n==-1:
            while min_heap and not state[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                state[min_heap[0][1]]=False    
                heapq.heappop(min_heap)
        elif max_heap and n==1:
            while max_heap and not state[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                state[max_heap[0][1]]=False    
                heapq.heappop(max_heap)
    while min_heap and not state[min_heap[0][1]]: heapq.heappop(min_heap)
    while max_heap and not state[max_heap[0][1]]: heapq.heappop(max_heap)
    
    if not min_heap and not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])