k, n = map(int, input().split())
arr = []
def solution(count, n):
    if n==count: 
        print(*arr)
        return
    for i in range(1, k+1):
        arr.append(i)
        solution(count+1, n)
        arr.pop()
        
solution(0, n)