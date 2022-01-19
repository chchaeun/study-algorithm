from collections import deque
def solution(places):
    answer = []
    for i in range(len(places)):
        answer.append(manhattan(places[i]))
    return answer

# manhattan 거리에 어긋나는지 판단
# 어긋나면 violation 함수로 보냄                
def manhattan(place):
    person = []
    for i in range(5):
        for j in range(5):
            if place[i][j]=="P":
                person.append([i, j])
    for i in range(len(person)):
        for j in range(i+1, len(person)):
            cal = abs(person[i][0]-person[j][0])+abs(person[i][1]-person[j][1])
            if cal <= 2:
                if not violation(place, person[i], person[j]): return 0
    return 1
    
# p1에서 p2까지 X를 거치지 않고 가는 거리가 2 이하인지 탐색            
def violation(place, p1, p2):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dq = deque([(p1[0], p1[1])])
    visited[p1[0]][p1[1]] = 1
    while dq:
        x, y = dq.popleft()
        if x == p2[0] and y==p2[1]:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0 and place[nx][ny] != 'X':
                dq.append((nx, ny))
                visited[nx][ny] = visited[x][y]+1
    if 1<=visited[p2[0]][p2[1]]<=3:
        return 0
    else:
        return 1    

test = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(test))