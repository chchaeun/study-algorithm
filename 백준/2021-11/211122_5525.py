import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

dq = deque()
top = -1
length = 2*n+1
result = 0
for elem in s:
    if len(dq)==0:
        if elem == 'I':
            dq.append(elem)
            top+=1
        continue
    if dq[top]=='I':
        if len(dq)==length:
            result+=1
            dq.popleft()
            dq.popleft()
            top-=2
        if elem == 'O':
            dq.append(elem)
            top+=1
        elif elem=='I':
            dq.clear()
            dq.append(elem)
            top=0
    elif dq[top]=='O':
        if elem == 'O':
            dq.clear()
            top=-1
        elif elem=='I':
            dq.append(elem)
            top+=1
print(result)


'''
# 모범답안
n = int(input())
m = int(input())
s = sys.stdin.readline()

cnt = 0
answer = 0
stack=[]

for i in range(m):
    if s[i] == "O":
        continue
    else:
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= n:
        answer += 1


print(answer)
'''