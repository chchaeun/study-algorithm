import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = max(arr), sum(arr)

while left < right:
    
    mid = (left + right) // 2
    temp = 0
    count = 0 
    for i in arr:
        if temp + i > mid:
            count += 1
            temp = 0
        temp += i
    count+=1

    if count == m:
        right = mid
    elif count > m:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)