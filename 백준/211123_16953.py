import sys

a, b = map(int, sys.stdin.readline().split())
result=0
while True:
    if b % 2 == 0:
        b = b//2
        result+=1
    elif b % 10 == 1:
        b = b//10
        result+=1
    else:
        result=-1
        break
    if b==a:
        result+=1
        break
    elif b<a:
        result=-1
        break
print(result)