import sys

n = int(sys.stdin.readline().strip())

large = list(map(int, sys.stdin.readline().split()))
small = large[:]
for i in range(1, n):
    arr = list(map(int, sys.stdin.readline().split()))
    large = [max(large[0], large[1])+arr[0],\
        max(large[0], large[1], large[2])+arr[1],\
        max(large[1], large[2])+arr[2]]
    small = [min(small[0], small[1])+arr[0],\
        min(small[0], small[1], small[2])+arr[1],\
        min(small[1], small[2])+arr[2]]
print(max(large), min(small))

'''
새로운 리스트를 만들어서 다음 리스트와 합친다.
메모리 초과 방지를 위해서 배열을 미리 다 할당하지 않는다.
아래로부터 위를 보는 방식
'''