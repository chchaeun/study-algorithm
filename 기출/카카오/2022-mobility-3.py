def solution(s, times):
    everyday = True

    current = list(map(int, s.split(":")))

    for time in times:
        new_time = current[:2]
        t_list = list(map(int, time.split(":")))

        for i in range(-4, 0):
            new_time.append(current[i] + t_list[i])

        limit = [12, 30, 24, 60, 60]
        print(new_time)
        for i in range(-1, -6, -1):
            if new_time[i] > limit[i]:
                new_time[i] -= limit[i]
                new_time[i-1] += 1
        
        current = new_time
        print(current)

print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))