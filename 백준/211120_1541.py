import sys 
from collections import deque
str = list(map(str, sys.stdin.readline().rstrip().split("-")))

dq = deque()

result=0
for i, s in enumerate(str):
    temp = s.split("+")
    for t in temp:
        if i==0:
            result += int(t)
        else:
            result -= int(t)
        
print(result)