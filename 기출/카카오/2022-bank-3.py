def solution(rooms):
    ring = 0
    visited = [False for _ in range(len(rooms))]

    for i in range(len(rooms)):
        if not visited[i]:
            ring += 1

            visited[i] = True
            next = rooms[i] - 1

            while not visited[next]:
                visited[next] = True
                next = rooms[next] - 1

    if ring > 1:
        ring -= 1

    return ring


arr = [i-1 for i in range(200000)]

print(solution(arr))
print(solution([3,1,2,4]))
print(solution([2,3,4,5,1]))
print(solution([1,2,3,4,5,6]))
print(solution([6,5,4,3,2,1]))
