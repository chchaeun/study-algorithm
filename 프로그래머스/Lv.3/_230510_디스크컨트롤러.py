import heapq
def solution(jobs):
    answer, now, jdx = 0, 0, 0
    start = -1
    exe = []
    jobs.sort()
    while jdx < len(jobs):
        for job in jobs[jdx:]:
            if start < job[0] <= now:
                heapq.heappush(exe, (job[1], job[0]))
                
        if len(exe) > 0:
            e = heapq.heappop(exe)
            start = now
            now += e[0]
            answer += now - e[1]
            jdx += 1
        else:
            now += 1

    return int(answer / len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]]))