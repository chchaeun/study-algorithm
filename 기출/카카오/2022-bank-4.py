def solution(jobs):
    stars = [0 for _ in range(101)]
    takens = [0 for _ in range(101)]

    first_job = jobs[0]
    current_job = first_job[2]
    current_time = first_job[0] + first_job[1]

    check_index = 1
    schedule = [current_job]

    while check_index < len(jobs):
        start = check_index

        if jobs[start][0] > current_time:
            current_time += 1
            continue

        for i, job in enumerate(jobs[start:]):
            request_time, require_time, id, star = job

            if request_time <= current_time:
                if current_job != id:
                    stars[id] += star
                    takens[id] += require_time
                else:
                    current_time += require_time
                check_index = start + i + 1
                
            else:
                check_index = start + i
                break

        current_job = stars.index(max(stars))
        if current_job != 0 and current_job != schedule[-1]:
            schedule.append(current_job)
        current_time += takens[current_job]

        stars[current_job] = 0
        takens[current_job] = 0
    
    while True:
        current_job = stars.index(max(stars))
        if current_job == 0:
            break
        if current_job != schedule[-1]:
            schedule.append(current_job)
            stars[current_job] = 0
            takens[current_job] = 0

    return schedule

solution([[1,5,2,3],[2,2,3,2],[3,1,3,3],[5,2,1,5],[7,1,1,1],[9,1,1,1],[10,2,2,9]])
solution([[1,2,1,5],[2,1,2,100],[3,2,1,5],[5,2,1,5]])
solution([[0,2,3,1],[5,3,3,1],[10,2,4,1]])
solution([[0,5,1,1],[2,4,3,3],[3,4,4,5],[5,2,3,2]])
solution([[0, 1, 1, 5], [5, 1, 1, 5], [100, 1, 1, 10]])

# from collections import deque

# def solution(jobs):
#     job_numbs = [[] for _ in range(101)]
#     answer = []
#     q = deque(jobs)
#     cur_time = 0

#     while q:
#         request_time, require_time, numb, pri = q.popleft()
#         answer.append(numb)
#         cur_time += require_time
#         while q and q[0][0] <= cur_time:
#             if q[0][2] == numb:
#                 request_time, require_time, numb, pri = q.popleft()
#                 cur_time += require_time
#             else:
#                 a, b, c, d = q.popleft()
#                 job_numbs[c].append([a, b, c, d])
        
#         Max = -1
#         next_num = 0
#         for i in range(1, 101):
#             total = 0
#             for j in range(len(job_numbs[i])):
#                 total += job_numbs[i][j][3]
#             if total > Max:
#                 Max = total
#                 next_num = i

#         tmp = job_numbs[next_num]
#         tmp.extend(list(q))
#         q = deque(tmp)
#         job_numbs[next_num] = []
    
#     return answer

