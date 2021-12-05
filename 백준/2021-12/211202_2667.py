import sys

n = int(sys.stdin.readline().strip())

table = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 탐색하기 위해 이동시킬 때 하나하나 더하고 빼지 말고 
# dx, dy 선언해서 for문 처리
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    # 이동할 수 없는 좌표일 때 False 리턴
    if x<0 or x>=n or y <0 or y>=n:
        return False
    
    if table[x][y] == 1:
        global count
        count +=1
        table[x][y] = 0
        # count하고 0으로 바꿈
        # 이동 후 dfs 호출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        # True를 리턴
        return True
    return False
        
count=0
total = 0
block = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            # block에 count를 추가
            # total을 하나 증가시키고 count 초기화
            block.append(count)
            total+=1
            count=0

block.sort()
print(total)
for b in block:
    print(b)