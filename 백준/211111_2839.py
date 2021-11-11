import sys
from collections import deque
n = int(sys.stdin.readline())
dq = deque()

sum = 0
while sum!=n:
    temp = sum + 5
    if temp < n:
        sum += 5
        dq.append(5)
    elif temp > n:
        break
    else:
        sum+=5       
        dq.append(5)
        result = len(dq)
        break

while sum!=n:
    temp = sum + 3
    if temp < n:
        sum += 3
        dq.append(3)
    elif temp > n:
        if len(dq)==0 or dq[0] == 3:
            result = -1
            break
        dq.popleft()
        sum -= 5
    else:
        sum+=3
        dq.append(3)
        result = len(dq)
        break

print(result)