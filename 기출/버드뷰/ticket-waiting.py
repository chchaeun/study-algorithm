from collections import defaultdict
def solution(waiting):
    answer = []
    id_dict = defaultdict(int)
    for w in waiting:
        if not id_dict[w]:
            id_dict[w] = 1
            answer.append(w)
    return answer

test_waiting = [
    [1, 5, 8, 2, 10, 5, 4, 6, 4, 8],
    [5, 4, 4, 3, 5]
]

for t in test_waiting:
    print(solution(t))