import sys; input=sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
machine = []
for i in range(len(room)):
    if room[i][0]==-1:
        machine.append(i)

def spread():
    nroom = [[0 for _ in range(c)] for _ in range(r)]
    dust = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(len(room)):
        for j in range(len(room[i])):
            # 먼지 있는 부분만
            if room[i][j]>0:
                # 몇 개 방향으로 퍼지는지
                count = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<r and 0<=ny<c and room[nx][ny]!=-1:
                        # 위쪽 먼지인지 아래쪽 먼지인지 구해서 공기청정기 돌렸을 때 방향 얻어냄
                        if nx<=machine[0]:
                            nx, ny = clean(nx, ny, machine[0], 1)
                        else:
                            nx, ny = clean(nx, ny, machine[1], -1)
                        # 얻어낸 방향으로 퍼뜨림
                        nroom[nx][ny] += room[i][j]//5
                        count+=1
                # 원래 먼지 있던 위치+몇 개 방향으로 퍼졌는지 저장
                dust.append((i, j, room[i][j], count))
    # 먼지도 공기청정기 돌렸을 때 방향에 저장
    for d in dust:
        if d[0]<=machine[0]:
            nx, ny = clean(d[0], d[1], machine[0], 1)
        else: 
            nx, ny = clean(d[0], d[1], machine[1], -1)
        nroom[nx][ny] += d[2] - (d[2]//5)*d[3]
        
    nroom[machine[0]][0] = -1
    nroom[machine[1]][0] = -1
    
    return nroom

def clean(nx, ny, mc, isTop):
    # 방향 같은 건 같은 숫자로, 다른 건 isTop으로 
    if (nx==0 or nx==r-1) and ny!=0:
        return nx, ny-1
    elif ny==0 and nx!=mc:
        return nx+isTop, ny
    elif nx==mc and ny!=c-1:
        return nx, ny+1
    elif ny==c-1 and nx!=0:
        return nx-isTop, ny
    return nx, ny
    
for _ in range(t):
    room = spread()

# 공기청정기 부분은 -1 이므로 2를 더해줌
answer = sum(list(map(sum, room)))+2
print(answer)
