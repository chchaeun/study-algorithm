def solution(plans):
    answer = []
    now = 0
    left = []
    for plan in plans:
        plan[1] = get_minutes(plan[1])
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])
    for plan, next in zip(plans, plans[1:]+[['end', 1440, 0]]):
        while left:
            done = now + left[-1][1]
            if done > plan[1]:
                left[-1][1] = done - plan[1]
                now = plan[1]
                break
            else:
                now += left[-1][1]
                answer.append(left[-1][0])
                left.pop()

        done = plan[1] + plan[2]
        if done > next[1]:
            left.append([plan[0], done - next[1]])
            now = next[1]
        else:
            now = done
            answer.append(plan[0])

    while left:
        now += left[-1][1]
        answer.append(left[-1][0])
        left.pop()
    return answer


def get_minutes(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

tc = [[[["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]], ["korean", "english", "math"]],
[[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]], ["science", "history", "computer", "music"]],
[[["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]], ["bbb", "ccc", "aaa"]]]

for t in tc:
    if solution(t[0]) == t[1]:
        print('pass')
    else:
        print('fail')