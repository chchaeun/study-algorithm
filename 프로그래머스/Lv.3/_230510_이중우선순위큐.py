import heapq

def solution(operations):
    hq = []

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == 'I':
            heapq.heappush(hq, num)
        if hq and op == 'D':
            if num == -1:
                heapq.heappop(hq)
            if num == 1:
                hq = heapq.nlargest(len(hq), hq)[1:]
                heapq.heapify(hq)
        
    if hq:
        return [max(hq), min(hq)]
    else:
        return [0, 0]

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])