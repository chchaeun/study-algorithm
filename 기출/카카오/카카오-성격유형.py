from collections import defaultdict

def solution(survey, choices):
    answer = []
    category = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    score = defaultdict(int)
    point = [-1, 3, 2, 1, 0, 1, 2, 3]
    for sur, cho in zip(survey, choices):
        if cho<4:
            score[sur[0]] += point[cho]
        elif cho>4:
            score[sur[1]] += point[cho]
    for cat in category:
        if score[cat[0]]<score[cat[1]]:
            answer.append(cat[1])
        else:
            answer.append(cat[0])
    return ''.join(answer)

print(solution(['AN', 'CF', 'MJ', 'RT', 'NA'], [5, 3, 2, 7, 5]))
print(solution(['TR', 'RT', 'TR'], [7,1,3]))