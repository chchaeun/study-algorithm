from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for c in course:
        combinated = []
        d = defaultdict(int)
        for order in orders:
            order_list = list(order)
            if c <= len(order_list):
                combinated.extend(combinations(order_list, c))
        for i in range(len(combinated)):
            combinated[i] = ''.join(sorted(list(combinated[i])))
            d[combinated[i]]+=1
        if d and max(d.values())>=2:
            for key in list(d.keys()):
                if d[key]==max(d.values()):
                    answer.append(key)
    answer.sort()
    return answer
    
test_orders = [
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
    ["XYZ", "XWY", "WXA"]
]

test_course = [
    [2,3,4],
    [2,3,5],
    [2,3,4]
]

for o, c in zip(test_orders, test_course):
    print(solution(o, c))