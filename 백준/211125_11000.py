from sys import stdin
import heapq

n = int(stdin.readline().strip())
lec=[]
result=0
for _ in range(n):
    lec.append(list(map(int, stdin.readline().split())))
lec.sort(key=lambda x:(x[0], x[1]))

class_room = []
heapq.heappush(class_room, lec[0][1])

for i in range(1, n):
    if class_room[0] > lec[i][0]:
        heapq.heappush(class_room, lec[i][1])
    else:
        heapq.heappop(class_room)
        heapq.heappush(class_room, lec[i][1])
print(len(class_room))

# deque로 했을 때 반례
# [1, 3], [2, 4], [3, 3] 이런 식을 들어왔을 때 
# 큐가 [3, 4]에서 3이 pop되고 3이 들어온다. 
# 이 때 3이 4 앞으로 가지 않으면 항상 인덱스 0번과 비교하기 때문에 오류 발생