from collections import defaultdict
def solution(clothes):
    answer = 1
    dict = defaultdict(int)
    for c in clothes:
        dict[c[1]]+=1
    for key in dict.keys():
        answer *= dict[key]+1
    return answer-1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))