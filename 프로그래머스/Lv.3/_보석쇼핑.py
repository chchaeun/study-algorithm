from collections import defaultdict

def solution(gems):
    gems_set = list(set(gems))
    start, end = 0, -1
    answer = [start, len(gems) - 1]
    count = defaultdict(int)

    while start < len(gems) and end < len(gems):
        if len(count) == len(gems_set):
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
            else:
                count[gems[start]] -= 1
                if count[gems[start]] == 0:
                    del count[gems[start]]
                start += 1
        else:
            end += 1
            if end == len(gems):
                break
            count[gems[end]] += 1

    return list(map(lambda x: x+1, answer))

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
